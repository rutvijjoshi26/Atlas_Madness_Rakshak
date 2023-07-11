import decord
import numpy as np
import multiprocessing as mp
import tensorflow as tf

# import tflite_runtime.interpreter as tflite


tflite_model_path = "obscenity_image.tflite"


# interpreter = tflite.Interpreter(model_path=tflite_model_path)
# interpreter.allocate_tensors()
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()


def predict(image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]["shape"]

    image = np.array(image, dtype=np.float32)

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


def process_video_multiprocessing(group_name, video_path, result):
    vr = decord.VideoReader(video_path, height=224, width=224, num_threads=3)
    frame_jump_unit = len(vr) // 4
    start = group_name * frame_jump_unit
    end = start + frame_jump_unit
    frames = vr.get_batch(range(start, end - 1, 144)).asnumpy()
    dict1 = {"SFW": 0, "NSFW": 0}
    for i in frames:
        preds = predict(i)
        if preds == "NSFW":
            dict1["NSFW"] += 1
        else:
            dict1["SFW"] += 1

    if dict1["NSFW"] > dict1["SFW"]:
        result.append("NSFW")
    else:
        result.append("SFW")


async def multiprocess(path):
    try:
        manager = mp.Manager()
        result = manager.list()
        l = []
        for i in range(4):
            p = mp.Process(target=process_video_multiprocessing, args=(i, path, result))
            p.start()
            l.append(p)

        for i in l:
            i.join()

        sfwc = 0
        nsfwc = 0
        for i in result:
            if i == "SFW":
                sfwc += 1
            elif i == "NSFW":
                nsfwc += 1
        if sfwc > nsfwc:
            return "SFW"
        else:
            return "NSFW"
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None
