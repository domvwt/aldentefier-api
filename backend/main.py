import uuid

import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image
from pathlib import Path

from fastai.learner import load_learner

def download_model(reference: str="latest"):
    if reference == "latest"
    ...

def list_available_models():
    ...

def preprocess_image():
    ...

def predict_image():
    if batch:
    ...

def show_activate_layers():
    ...

def show_image_heatmap():
    ...


print("Current directory: " + str(Path.cwd()))

model = load_learner("backend/models/aldentefier-0.1.pkl")
print(model)
