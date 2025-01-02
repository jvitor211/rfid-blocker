import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RFID Blocker"
    API_VERSION: str = "v1.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()