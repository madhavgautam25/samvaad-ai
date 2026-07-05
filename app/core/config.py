from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")

    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")
    MODEL_NAME = os.getenv("MODEL_NAME")

    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE")

    DEBUG = os.getenv("DEBUG") == "True"

settings = Settings()