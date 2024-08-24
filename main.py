from fastapi import FastAPI
from src.routes import models, gpt,views

app = FastAPI()
app.include_router(gpt.router)
app.include_router(models.router)
app.include_router(views.router)