from pathlib import Path

import uvicorn
from fastai.basics import load_learner
from fastai.learner import Learner
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIRECTORY = Path(__file__).parent.absolute()
RELATIVE_MODEL_PATH = "models/aldentefier-0.1.pkl"
ABSOLUTE_MODEL_PATH = BASE_DIRECTORY / RELATIVE_MODEL_PATH

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictOut(BaseModel):
    predicted_class: str
    likelihood: float


@app.get("/")
def read_root():
    return {
        "message": "Aldentefier ready - visit /docs or /redoc for API documentation."
    }


@app.post("/predict", response_model=PredictOut)
def predict_image(
    image: bytes = File(
        ...,
        description="Image sent to model for class prediction - required as binary.",
    )
):
    model = load_learner(ABSOLUTE_MODEL_PATH)
    pred = model.predict(image)
    return {"predicted_class": pred[0], "likelihood": max(pred[2])}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
