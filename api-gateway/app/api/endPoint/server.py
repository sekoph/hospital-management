from fastapi import FastAPI

from app.api.endPoint.authRoutes import app as auth_router
from app.api.endPoint.patientRoutes import app as patient_router
from app.api.endPoint.docterRoutes import app as doctor_router
from app.api.endPoint.bookingRoutes import app as appointment_router

application = FastAPI()

application.include_router(auth_router, tags=["auth"])
application.include_router(patient_router, tags=["patient"])
application.include_router(doctor_router, tags=["doctor"])
application.include_router(appointment_router, tags=["appointment"])
