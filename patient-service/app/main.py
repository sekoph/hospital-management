from fastapi import FastAPI, Depends
from app.api.endpoints.patientInsuranceRoute import patient_insurance_router
from app.api.endpoints.patientRoute import patient_router
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
import uvicorn
import webbrowser
import asyncio
from app.kafka.consumer.patientConsumer import PatientConsumer
from app.db.session import session_local

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    db_session = session_local()
    patient_kafka_consumer = PatientConsumer(bootstrap_servers=settings.bootstrap_servers, db=db_session)
    asyncio.create_task(patient_kafka_consumer.start())


allowed_origins = settings.ALLOWED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(patient_router)
app.include_router(patient_insurance_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8001/docs")
    uvicorn.run(app, host="0.0.0.0", port=8001)