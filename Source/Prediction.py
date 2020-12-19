import cv2
import tensorflow as tf
from PIL import Image

model = tf.keras.models.load_model("Source/model_.h5")

def prepare(filepath):
    width = 100
    hight = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (width, hight))
    return new_array.reshape(-1, width, hight, 1)

def predicting(filepath):
    prediction = model.predict([prepare(filepath)])
    return int(prediction[0][0])
""""
def checkcropedimages(result):
    indexes = []
    for index in range(1, result):
        chance = []
        path = str(index)+'.jpg'
        for angle in range(-5,6):
            img = Image.open(path)
            img = img.rotate(angle*1)
            img.save('rotated_'+path)
            if predicting('rotated_'+path):
                chance.append(1)
        if len(chance) > 0:
            indexes.append(index)
    return indexes
"""
