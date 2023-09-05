import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
#from utils import predict_label
from PIL import Image
import numpy as np
import os
st.title("emotion detection")

st.write("Predict the emotion that is being represented in the image.")

model = load_model("model.h5")
l=[ 'angry',
    'disgusted',
    'fearful',
    'happy',
    'neutral',
    'sad',
    'surprised']

#model = load_model("model.h5")
model_path = os.path.join(os.getcwd(), "model.h5")

if os.path.exists(model_path):
    model = load_model(model_path)
else:
    st.write("Model file 'model.h5' not found.")
uploaded_file = st.file_uploader(
    "Upload an image of a emotion :", type="jpeg"
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


st.write("If you would not like to upload an image, you can use the sample image instead:")
sample_img_choice = st.button("Use Sample Image")

if sample_img_choice:
    image1 = Image.open("seed_charlock.png")
    image1=image.smart_resize(image1,(256,256))
    img_array = image.img_to_array(image1)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array/255.0
    predictions = model.predict(img_array)
    label=l[np.argmax(predictions)]
    st.markdown(
        f"<h2 style='text-align: center;'>{label}</h2>",
        unsafe_allow_html=True,
    )
