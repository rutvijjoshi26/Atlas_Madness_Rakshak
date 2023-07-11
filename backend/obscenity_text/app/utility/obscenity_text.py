import pickle
import nltk 
from datetime import datetime
import numpy as np
import tensorflow as tf


from ..utility.utils import preprocess_test
from ..schema.nsfw import FileMetadata
from ..database.connection import obscenity_collection


tokenizer_file = 'word_index.pkl'
with open(tokenizer_file, 'rb') as handle:
    word_index = pickle.load(handle)


interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def remove_empty_lines(text):
    lines=nltk.sent_tokenize(text)
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    return non_empty_lines


async def predict_obscenity(lines: list):
    try:
        text_sentence = " ".join(lines)
        processed_sentence = preprocess_test(text_sentence)
        custom_sequence = []
        words = processed_sentence.split()
        for word in words:
            if word in word_index:
                custom_sequence.append(word_index[word])
        
        max_length = input_details[0]['shape'][1]
        custom_padded_sequence = np.zeros((1, max_length), dtype=np.float32)
        custom_padded_sequence[0, :len(custom_sequence)] = custom_sequence[:max_length]

        interpreter.set_tensor(input_details[0]['index'], custom_padded_sequence)
        interpreter.invoke()

        output = interpreter.get_tensor(output_details[0]['index'])
        class_label = 'NSFW' if output >= 0.5 else 'SFW'

        return class_label

    except Exception as e:
        # Handle any potential errors or exceptions
        print("Error occurred during prediction:", str(e))
        return None



async def process_text_obscenity(text,client_host):
    lines=remove_empty_lines(text)
    identifier=" ".join(lines)[:13].lower()
    res= await predict_obscenity(lines)
    try:
        filemetadata=FileMetadata(
            content= identifier,
            size=len(lines),
            date_of_acquisition=datetime.now(),
            source=client_host,
            result=res,
            type_of_file="text"
        )
        query={"content":identifier}
        update={"$inc":{"counter":1}}
        result_of_updation=obscenity_collection.update_one(query,update)
        if result_of_updation.modified_count == 0:
            obscenity_collection.insert_one(filemetadata.dict())
            print("Entry made in database")
        else:
            print("Counter Increased")
    except Exception as e:
        print(f"Error occurred while interacting with the database: {str(e)}")

    return res

    
        





