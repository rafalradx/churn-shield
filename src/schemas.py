from pydantic import BaseModel, RootModel
from typing import Dict

class InputData(BaseModel):
    is_tv_subscriber: int
    is_movie_package_subscriber: int
    subscription_age: float
    bill_avg: float
    remaining_contract: float
    service_failure_count: int
    download_avg: float
    upload_avg: float
    download_over_limit: int

# Model dla predictions
class Predictions(BaseModel):
    predictions: Dict[str, float]  # Klucze to nazwy modeli, wartości to float

# Model dla całości żądania
class RecommendationRequest(BaseModel):
    input_data: InputData
    predictions: Dict[str, float]  # Tu bezpośrednio używamy słownika
