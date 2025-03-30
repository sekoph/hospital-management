from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from crud.patientInsuranceCrud import (
    get_all_patients_insurances,
    create_patient_insurance,
    update_patient_insurance_info,
    get_insurance_info_by_patient_id,
    delete_patient_insurance_info
)


from schemas.patientInsuranceSchema import (
    PatientInsuranceSchema,
    PatientInsuranceCreateSchema,
    PatientInsuranceUpdateSchema
)

from utils.db import get_db

patient_insurance_router = APIRouter(
    prefix="/patient_insurance",
    tags=["Patients Insurance Information"]
)


@patient_insurance_router.get(
    "/",
    response_model=List[PatientInsuranceSchema],
    status_code=200,
    summary="Get all patients insurance information",
    description="Get all patients insurance information"
)
async def get_patients_insurance_info_router(db: Session = Depends(get_db)):
    return await get_all_patients_insurances(db=db)


@patient_insurance_router.post(
    "/",
    response_model=PatientInsuranceSchema,
    status_code=201,
    summary="Create a patient insurance information",
    description="Create a patient insurance information"
)
async def create_patient_insurance_route(patient_insurance: PatientInsuranceCreateSchema, db: Session = Depends(get_db)):
    return await create_patient_insurance(db=db, patient_insurance=patient_insurance)


@patient_insurance_router.patch(
    "/{patient_id}",
    response_model=PatientInsuranceSchema,
    status_code=200,
    summary="Update a patient insurance information",
    description="Update a patient insurance information"
)
async def update_patient_insurance_info_route(patient_id: str, patient_insurance: PatientInsuranceUpdateSchema, db: Session = Depends(get_db)):
    return await update_patient_insurance_info(db=db, patient_id=patient_id, patient_insurance=patient_insurance)


@patient_insurance_router.get(
    "/{patient_id}",
    response_model=PatientInsuranceSchema,
    status_code=200,
    summary="Get a patient insurance information",
    description="Get a patient insurance information"
)
async def get_patient_insurance_info_route(patient_id: str, db: Session = Depends(get_db)):
    return await get_insurance_info_by_patient_id(db=db, patient_id=patient_id)


@patient_insurance_router.delete(
    "/{patient_id}",
    status_code=200,
    summary="Delete a patient insurance information",
    description="Delete a patient insurance information"
)
async def delete_patient_insurance_info_route(patient_id: str, db: Session = Depends(get_db)):
    deleted_info =  await delete_patient_insurance_info(db=db, patient_id=patient_id)
    if deleted_info:
        return {"message": "Patient insurance information deleted successfully"}