import tensorflow as tf
from PIL import Image
import numpy as np


tflite_model_path = "obscenity_image.tflite"
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()


input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


async def predict_one_tflite(path):
    try:
        # Load and preprocess the image
        image = Image.open(path)
        image = image.resize((224, 224), resample=Image.BILINEAR)
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)

        # Set input tensor
        input_tensor = np.array(image_array, dtype=np.float32)
        interpreter.set_tensor(input_details[0]["index"], input_tensor)

        # Perform inference
        interpreter.invoke()

        # Get output tensor
        output_tensor = interpreter.get_tensor(output_details[0]["index"])

        # Convert output tensor to probabilities
        result = 1 / (1 + np.exp(-output_tensor))

        if result[0][0] <= 0.5:
            return "NSFW"

        return "SFW"
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None
