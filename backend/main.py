import os
import uuid

import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image
from pathlib import Path

from dotenv import load_dotenv
from google.cloud import storage
from fastai.basics import load_learner


load_dotenv()

# https://elements.heroku.com/buildpacks/buyersight/heroku-google-application-credentials-buildpack


def download_model(reference: str = "latest"):
    if reference == "latest":
        pass
    ...


def download_model(bucket_name, model_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(model_name)
    blob.download_to_filename(destination_file_name)

    print("Model {} downloaded to {}.".format(model_name, destination_file_name))


def download_test_images():
    ...


def list_available_models():
    ...


def preprocess_image():
    ...


def predict_image():
    if batch:
        pass
    ...


def show_activation_areas():
    ...


def show_image_heatmap():
    ...


def main():
    download_model(os.environ.get("GSBUCKET"), "models/aldentefier-0.1.pkl", "models")
    model = load_learner("backend/models/aldentefier-0.1.pkl")
    print(model)


if __name__ == "__main__":
    main()
