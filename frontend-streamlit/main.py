import os
import requests
import streamlit as st


from PIL import Image
from dotenv import load_dotenv


load_dotenv()
API_PREDICT_ROUTE = os.environ.get("API_PREDICT_ROUTE")


st.title("Pasta Aldentefier")

image = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])

if st.button("Predict!"):
    if image is not None:
        image_bytes = image.read()
        st.image(image_bytes, width=400)
        payload = {"image": image_bytes}
        r = requests.post(API_PREDICT_ROUTE, files=payload)
        print(r.text)
        r_json = r.json()
        pred_class = r_json.get("predicted_class")
        likelihood = r_json.get("likelihood")
        st.header("Prediction")
        st.subheader(f"Pasta: {pred_class}")
        st.subheader(f"Likelihood: {likelihood}")

