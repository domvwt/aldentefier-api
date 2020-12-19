import os
import requests
import streamlit as st


from PIL import Image
from dotenv import load_dotenv


load_dotenv()
API_PREDICT_ROUTE = os.environ.get("API_PREDICT_ROUTE")
API_ROOT = os.environ.get("API_ROOT")


st.set_page_config(
    page_title="Aldentefier",
    page_icon=":spaghetti:",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Pasta Aldentefier :spaghetti:")

st.markdown("""
    The Pasta Aldentefier is an image recognition app that
    can *somewhat* reliably identify images of dry pasta. 


    The model has been trained on Google image search results to recognise:
    * Farfalle
    * Fusilli
    * Macaroni
    * Penne
    * Rigatoni
    * Spaghetti
""")

r = requests.get(API_ROOT)
if not r.ok:
    st.markdown(":no_entry_sign: API Down, please try again later!")

st.subheader("Choose an image:")

image = st.file_uploader("", type=["png", "jpg", "jpeg"])

button = st.button("Predict!")

col1, col2 = st.beta_columns(2)

st.spinner()

slot1 = col1.empty()
slot2 = col1.empty()
slot3 = col1.empty()
slot4 = col2.empty()
slot5 = col2.empty()

if image is not None:
    image_bytes = image.read()
    slot4.markdown("*Your image:*")
    slot5.image(image_bytes, use_column_width=True)

if button and image is not None:
    with st.spinner():
        payload = {"image": image_bytes}
        r = requests.post(API_PREDICT_ROUTE, files=payload)
        print(r.text)
        r_json = r.json()
        pred_class = r_json.get("predicted_class")
        likelihood = r_json.get("likelihood")
        slot1.header("Prediction")
        if likelihood > 0.9:
            slot2.markdown(f"> **Pasta Type:** *{pred_class.capitalize()}!*")
            slot3.markdown(f"> **Likelihood:** *{round(likelihood * 100, 2)}%*")
            st.balloons()
        elif likelihood > 0.7:
            slot2.markdown(f"> **Pasta Type:** *Is it {pred_class.capitalize()}?*")
            slot3.markdown(f"> **Likelihood:** *{round(likelihood * 100, 2)}%*")
        else:
            slot2.markdown(f"> **Pasta Type:** *I don't know* :confused:")
            slot3.markdown(f"> **Likelihood:** *--%*")


st.markdown("----")
st.markdown(
    "[Github](https://github.com/domvwt/aldentefier-api) | [LinkedIn](https://www.linkedin.com/in/dominic-thorn/)"
)
