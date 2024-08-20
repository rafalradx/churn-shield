import os
import numpy as np
import joblib
import pandas as pd
from tensorflow.keras.models import load_model
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()

models_path = 'models/'

models = []

# Load models
for model_file in os.listdir(models_path):
    model_path = os.path.join(models_path, model_file)

    # Load .keras models
    if model_path.endswith(".keras"):
        models.append(load_model(model_path))
    # Load scaler
    elif model_path.endswith("scaler.pkl"):
        scaler = joblib.load(model_path)
    # Load .pkl models
    elif model_path.endswith(".pkl"):
        models.append(joblib.load(model_path))

# Scaler features
features_to_scale = [
    "subscription_age",
    "bill_avg",
    "reamining_contract",
    "service_failure_count",
    "download_avg",
    "upload_avg",
    ]

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "models":models})

class InputData(BaseModel):
    is_tv_subscriber: int
    is_movie_package_subscriber: int
    subscription_age: float
    bill_avg: float
    remaining_contract: float
    service_failure_count: int
    download_avg: float
    upload_avg: float
    download_over_limit: float

@app.post("/predict/")
def predict(data: InputData):
    predictions = {}

    input_data = pd.DataFrame({
        "is_tv_subscriber": [data.is_tv_subscriber],
        "is_movie_package_subscriber": [data.is_movie_package_subscriber],
        "subscription_age": [data.subscription_age],
        "bill_avg": [data.bill_avg],
        "reamining_contract": [data.remaining_contract],
        "service_failure_count": [data.service_failure_count],
        "download_avg": [data.download_avg],
        "upload_avg": [data.upload_avg],
        "download_over_limit": [data.download_over_limit]
    })

    input_data[features_to_scale] = scaler.transform(input_data[features_to_scale])

    # Calculate probability for each model
    for model in models:
        model_name = model.__class__.__name__
        if model_name == "Sequential":
            prediction = model.predict(input_data.values, verbose = 0)[0][0]
            probability = float(prediction)
        else:
            prediction = model.predict_proba(input_data)[:, 1][0]
            probability = float(prediction)

        predictions[model_name] = probability

    return predictions