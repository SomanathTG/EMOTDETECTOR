import streamlit as st
import os
from tensorflow import keras
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.preprocessing import image
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
import pathlib
from keras.models import load_model
import matplotlib.image as mpimg


# # Define the home function
# def home():
#     st.write("## Introduction")
#     st.write("This app uses to dectect the emotion of the person")
   
    
#     st.write("This Data contains around 75k images of size 50x50 distributed under 5 categories.")
#     st.write("'Five' -> 0")
#     st.write("'Zero' -> 1")
#     st.write("'Two' -> 2")
#     st.write("'Four' -> 3")
#     st.write("'One' -> 4")
#     st.write("'Three' -> 5")


# Define the prediction function
def prediction():
    
    st.write("Predict the Rice image that is being represented in the image")
    
    # Define the input fields
    model = load_model("model.h5")
    l=[ 'angry',
    'disgusted',
    'fearful',
    'happy',
    'neutral',
    'sad',
    'surprised']

    
    uploaded_file = st.file_uploader(
        "Upload an image of a Rice Image:", type="jpg"
    )
    predictions=-1
    if uploaded_file is not None:
       image1 = Image.open(uploaded_file)
       image1=image.smart_resize(image1,(112,112))
       img_array = image.img_to_array(image1)
       img_array = np.expand_dims(img_array, axis=0)
       img_array = img_array/255.0
       predictions = model.predict(img_array)
       label=l[np.argmax(predictions)]
    st.write("### Prediction Result")
    if st.button("Predict"): 
        if uploaded_file is not None:
        image1 = Image.open(uploaded_file)
        st.image(image1, caption="Uploaded Image", use_column_width=True)
        st.markdown(
            f"<h2 style='text-align: center;'>Image of {label}</h2>",
            unsafe_allow_html=True,
        )
       else:
           st.write("Please upload file or choose sample image.")
      

def main():
    st.set_page_config(page_title="Rice Image Classification", page_icon=":heart:")
    st.markdown("<h1 style='text-align: center; color: white;'>Rice Image Classification</h1>", unsafe_allow_html=True)
    
    # Only show the "Classification" page
    prediction()
main()
