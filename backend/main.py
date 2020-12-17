from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from fastai.basics import load_learner
from fastai.learner import Learner
from fastapi import FastAPI, File
from google.cloud import storage
from pydantic import BaseModel

BASE_DIRECTORY = Path(__file__).parent.absolute()
RELATIVE_MODEL_PATH = "models/aldentefier-0.1.pkl"
ABSOLUTE_MODEL_PATH = BASE_DIRECTORY / RELATIVE_MODEL_PATH

load_dotenv()
app = FastAPI()


class PredictOut(BaseModel):
    predicted_class: str
    likelihood: float


@app.get("/")
def read_root():
    return {"message": "Aldentefier ready - send an image to /predict or visit /docs for API documentation."}


@app.post("/predict", response_model=PredictOut)
def predict_image(
    image: bytes = File(
        ..., description="Image sent to model for class prediction - required as bytes."
    )
):
    model = load_learner(ABSOLUTE_MODEL_PATH)
    pred = model.predict(image)
    return {"predicted_class": pred[0], "likelihood": max(pred[2])}


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
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
