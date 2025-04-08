from fastapi import FastAPI, Depends
import uvicorn
import webbrowser
from fastapi.middleware.cors import  CORSMiddleware
from app.config.settings import settings
from app.kafka.consumer.docterConsumer import DocterConsumer
from app.db.session import session_local
from fastapi import Depends
from sqlalchemy.orm import Session
import asyncio

from app.api.endpoints.doctorSpecializationRoute import doctor_specalization_router
from app.api.endpoints.doctorRoute import docter_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    db_session = session_local()
    docter_kafka_consumer = DocterConsumer(bootstrap_servers=settings.bootstrap_servers, db =db_session )
    asyncio.create_task(docter_kafka_consumer.start())
    
    
allowed_origins = settings.ALLOWED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(doctor_specalization_router)
app.include_router(docter_router)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8002/docs")
    uvicorn.run(app, host="0.0.0.0", port=8002)