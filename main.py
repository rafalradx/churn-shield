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

for model_file in os.listdir(models_path):
    model_path = os.path.join(models_path, model_file)

    if model_path.endswith(".keras"):
        models.append(load_model(model_path))
    elif model_path.endswith(".pkl"):
        models.append(joblib.load(model_path))


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "models":models})

class InputData(BaseModel):
    is_tv_subscriber: bool
    is_movie_package_subscriber: bool
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

    sequential_input_data = np.array([[
        data.is_tv_subscriber,
        data.is_movie_package_subscriber,
        data.subscription_age,
        data.bill_avg,
        data.remaining_contract,
        data.service_failure_count,
        data.download_avg,
        data.upload_avg,
        data.download_over_limit
    ]])

    input_data = {
        "is_tv_subscriber": [data.is_tv_subscriber],
        "is_movie_package_subscriber": [data.is_movie_package_subscriber],
        "subscription_age": [data.subscription_age],
        "bill_avg": [data.bill_avg],
        "reamining_contract": [data.remaining_contract],
        "service_failure_count": [data.service_failure_count],
        "download_avg": [data.download_avg],
        "upload_avg": [data.upload_avg],
        "download_over_limit": [data.download_over_limit]
    }

    input_df = pd.DataFrame(input_data)

    for model in models:
        model_name = model.__class__.__name__
        if model_name == "Sequential":
            prediction = model.predict(sequential_input_data)
            probability = 1.0 - float(prediction[0][0])
        else:
            prediction = model.predict_proba(input_df)
            probability = prediction[0][1]

        predictions[model_name] = probability

    return predictions