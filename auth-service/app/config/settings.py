import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    # app details
    API_TITLE = os.getenv("APP_NAME")
    bootstrap_servers=("kafka1-hospital:9092")
    
    # security
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # cors
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", " ").split(",")

    # database
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    
    
settings = Settings()