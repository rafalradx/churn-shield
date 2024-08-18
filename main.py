import os
from tensorflow.keras.models import load_model
from fastapi import FastAPI, Request, HTTPException, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np

templates = Jinja2Templates(directory="templates")

app = FastAPI()

models_path = 'models/'
models_dict = {model_name: load_model(os.path.join(models_path, model_name)) for model_name in os.listdir(models_path) if model_name.endswith('.keras')}
models = models_dict.keys()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    print(models)
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

# Endpoint do przewidywania
@app.post("/predict/")
def predict(model_name: str, data: InputData):
    # Sprawdzenie, czy model istnieje w słowniku
    if model_name not in models_dict:
        raise HTTPException(status_code=404, detail="Model not found")

    model = models_dict[model_name]

    input_data = np.array([[
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

    # Dokonanie predykcji
    prediction = model.predict(input_data)

    # Interpretacja wyniku
    probability = 1.0 - float(prediction[0][0])

    return {"probability": probability}