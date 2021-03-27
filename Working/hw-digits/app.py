import sys
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow.keras as keras
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import pred


def draw():
    b_width = st.sidebar.slider('Brush Width: ', 1, 50, 10)
    realtime = st.sidebar.checkbox('Update in realtime', True)

    image_data = st_canvas(
        brush_width=b_width, 
        brush_color='#FFF',
        background_color='#000',
        height=280,
        width=280,
        drawing_mode=True,
        key="canvas"
    )
    try:
        arr = np.array(image_data, dtype=np.uint8)
        img = Image.fromarray(arr)
        img = img.convert('L')
        img = img.resize((28, 28))
        img.save('test.jpg')
        arr, ans = pred.prediction()
        return ans
    except:
        pass


if __name__ == '__main__':
    st.markdown('''
        # Hand Written Digits Recongnize with Keras

        a project developed by Ex10si0n powered by `Streamlit` and `Keras`
    ''')
    st.sidebar.markdown('''
        # Playable Stuff
        At here you can play with the parameters that could affect the result.
    ''')

    
    # img = Image.open('test.jpg')
    # img_arr = np.reshape(img, (1, 28, 28))
    # if img_arr.any() != np.zeros((1, 28, 28)).any():
    #    ans = draw()
    
    ans = draw()



    st.markdown('## predict: ' + str(ans))

