import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
from PIL import Image


def prediction():

    model = keras.models.load_model('MNIST.h5')


    img = Image.open('test.jpg')
    img_arr = np.reshape(img, (1, 28, 28))
    predict = model.predict(img_arr)


    max_ = -1
    max_i = 0
    softmax = predict.tolist()[0]


    for i in range(len(softmax)):
       if softmax[i] >= max_:
           max_ = softmax[i]
           max_i = i
    return str(predict), str(max_i)
