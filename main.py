from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.routes import models, gpt, views

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(gpt.router)
app.include_router(models.router)
app.include_router(views.router)
