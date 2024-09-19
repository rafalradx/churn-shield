from fastapi import APIRouter
from src.dependencies.gpt import generate_suggestion
from src.schemas import RecommendationRequest

router = APIRouter(prefix="/gpt", tags=["gpt"])


@router.post("/recommend/")
async def recommend(data: RecommendationRequest):
    recommendation = await generate_suggestion(data.input_data, data.predictions)
    return {"recommendation": recommendation}
