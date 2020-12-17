import os

import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile

from fastai.vision.core import Image
from pathlib import Path
from dotenv import load_dotenv

from google.cloud import storage
from fastai.basics import load_learner
from fastai.learner import Learner


BASE_DIRECTORY = Path(__file__).parent.absolute()
RELATIVE_MODEL_PATH = "models/aldentefier-0.1.pkl"
ABSOLUTE_MODEL_PATH = BASE_DIRECTORY/RELATIVE_MODEL_PATH

load_dotenv()
app = FastAPI()

# https://elements.heroku.com/buildpacks/buyersight/heroku-google-application-credentials-buildpack


@app.get("/")
def read_root():
    return {"message": "Welcome to Aldentefier"}


@app.post("/predict")
def predict_image(image: bytes = File(...)):
    model = load_learner(MODEL_PATH)
    pred = model.predict(image)
    return {"prediction": pred[0]}


def download_model(bucket_name, model_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(model_name)
    blob.download_to_filename(destination_file_name)


def main(relative_path, absolute_path):
    if not Path(absolute_path).is_file():
        print(f"Downloading model to: {absolute_path}...")
        download_model(os.environ.get("GSBUCKET"), relative_path, str(absolute_path))
        print("Complete.")
    else:
        print(f"Found model: {absolute_path}")


if __name__ == "__main__":
    main(RELATIVE_MODEL_PATH, ABSOLUTE_MODEL_PATH)
    # uvicorn.run("main:app", host="0.0.0.0", port=8080)
