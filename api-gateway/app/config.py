import os
from  dotenv import load_dotenv
load_dotenv()

class Settings:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', "30"))
    ALGORITHM = os.environ.get('ALGORITHM')
    GATEWAY_TIMEOUT: int = 59
    
    AUTH_SERVICE_URL = os.environ.get('AUTH_SERVICE_URL')
    PATIENT_SERVICE_URL = os.environ.get('PATIENT_SERVICE_URL')
    DOCTOR_SERVICE_URL = os.environ.get('DOCTOR_SERVICE_URL')
    APPOINTMENT_SERVICE_URL = os.environ.get('APPOINTMENT_SERVICE_URL')
    
    
settings = Settings()