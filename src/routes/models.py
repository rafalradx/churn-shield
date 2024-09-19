from fastapi import APIRouter
from src.schemas import InputData
from src.dependencies import models

router = APIRouter(prefix="/models", tags=["models"])


@router.post("/predict/")
async def predict(data: InputData):
    predictions = await models.predict(data)
    return predictions
