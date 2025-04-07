from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from app.db.session import get_db

# import crud functions
from app.crud.patientCrud import (
    get_all_patients,
    create_patient,
    update_patient,
    get_patient_by_id,
    delete_patient
    )

# immport schemas
from app.schemas.patientSchema import (
    PatientSchema,
    PatientCreateSchema,
    PatientUpdateSchema)


from app.security.authMiddleware import get_current_user



patient_router = APIRouter(
    prefix="/patient",
    tags=["Patients"],
    # dependencies=[Depends(get_current_user)]
)


@patient_router.get(
    "/",
    response_model=List[PatientSchema],
    status_code=200,
    summary="Get all patients",
    description="Get all patients"
)
async def get_patients_router(db: Session = Depends(get_db)):
    patients = await get_all_patients(db=db)
    return patients


@patient_router.post(
    "/",
    response_model=PatientSchema,
    status_code=201,
    summary="Create a patient",
    description="Create a patient"
)
async def create_patient_route(patient: PatientCreateSchema, db: Session = Depends(get_db)):
    return await create_patient(db=db, patient=patient)


@patient_router.patch(
    "/{patient_id}",
    response_model=PatientSchema,
    status_code=200,
    summary="Update a patient",
    description="Update a patient"
)
async def update_patient_route(patient_id: str, patient: PatientUpdateSchema, db: Session = Depends(get_db)):
    return await update_patient(db=db, patient_id=patient_id, patient=patient)


@patient_router.get(
    "/{patient_id}",
    response_model=PatientSchema,
    status_code=200,
    summary="Get a patient by id",
    description="Get a patient by id"
)
async def get_patient_by_id_route(patient_id: str, db: Session = Depends(get_db)):
    return await get_patient_by_id(db=db, patient_id=patient_id)



@patient_router.delete(
    "/{patient_id}",
    status_code=200,
    summary="Delete a patient",
    description="Delete a patient"
)
async def delete_patient_route(patient_id: str, db: Session = Depends(get_db)):
    deleted_patient = await delete_patient(db=db, patient_id=patient_id)
    if deleted_patient:
        return {"message": "Patient deleted successfully"}