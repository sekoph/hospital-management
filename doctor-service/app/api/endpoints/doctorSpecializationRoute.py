from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from db.session import get_db

from crud.doctorSpecializationCrud import (
    get_all_doctor_specializations,
    create_doctor_specialization,
    get_doctor_specialization_by_id,
    update_doctor_specialization,
    delete_doctor_specialization
)


from schemas.doctorSpecializationSchema import (
    DoctorSpecializationSchema,
    DoctorSpecializationCreateSchema,
    DoctorSpecializationUpdateSchema
)

doctor_specalization_router = APIRouter(
    prefix="/doctor_specialization",
    tags=["Doctor Specialization"]
)

@doctor_specalization_router.get(
    "/",
    response_model=List[DoctorSpecializationSchema],
    status_code=200,
    summary="Get all doctor specializations",
    description="Get all doctor specializations"
)
async def get_doctor_specializations_router(db: Session = Depends(get_db)):
    return await get_all_doctor_specializations(db=db)


@doctor_specalization_router.post(
    "/",
    response_model=DoctorSpecializationSchema,
    status_code=201,
    summary="Create a doctor specialization",
    description="Create a doctor specialization"
)
async def create_doctor_specialization_router(doctor_specialization: DoctorSpecializationCreateSchema, db: Session = Depends(get_db)):
    return await create_doctor_specialization(db=db, doctor_specialization=doctor_specialization)


@doctor_specalization_router.get(
    "/{doctor_specialization_id}",
    response_model=DoctorSpecializationSchema,
    status_code=200,
    summary="Get a doctor specialization by id",
    description="Get a doctor specialization by id"
)
async def get_doctor_specialization_by_id_router(doctor_specialization_id: str, db: Session = Depends(get_db)):
    return await get_doctor_specialization_by_id(db=db, doctor_specialization_id=doctor_specialization_id)


@doctor_specalization_router.patch(
    "/{doctor_specialization_id}",
    response_model=DoctorSpecializationSchema,
    status_code=200,
    summary="Update a doctor specialization",
    description="Update a doctor specialization"
)
async def update_doctor_specialization_router(doctor_specialization_id: str, doctor_specialization: DoctorSpecializationUpdateSchema, db: Session = Depends(get_db)):
    return await update_doctor_specialization(db=db, doctor_specialization_id=doctor_specialization_id, doctor_specialization=doctor_specialization)


@doctor_specalization_router.delete(
    "/{doctor_specialization_id}",
    status_code=200,
    summary="Delete a doctor specialization",
    description="Delete a doctor specialization"
)
async def delete_doctor_specialization_router(doctor_specialization_id: str, db: Session = Depends(get_db)):
    deleted = await delete_doctor_specialization(db=db, doctor_specialization_id=doctor_specialization_id)
    if deleted:
        return {"message": "Doctor specialization deleted successfully"}