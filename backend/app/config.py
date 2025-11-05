# app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FESUP2026"
    debug: bool = True
    secret_key: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()