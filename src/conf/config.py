from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings
from typing import Optional

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)


class Settings(BaseSettings):

    openai_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
