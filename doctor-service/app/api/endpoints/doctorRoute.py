from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from app.db.session import get_db

from app.crud.doctorCrud import (
    get_all_doctors,
    create_doctor,
    get_doctor_by_id,
    update_docter,
    delete_doctor
)

from app.schemas.doctorSchema import (
    DoctorSchema,
    DocterCreateSchema,
    DoctorUpdateSchema
)


docter_router = APIRouter(
    prefix="/doctor",
    tags=["Doctors endpoints"]
)

@docter_router.get(
    "/",
    response_model=List[DoctorSchema],
    status_code=200,
    summary="Get all docters",
    description="Get all docters"
)
async def get_docters_router(db: Session = Depends(get_db)):
    return await get_all_doctors(db=db)


@docter_router.post(
    "/",
    response_model=DoctorSchema,
    status_code=201,
    summary="Create a doctor",
    description="Create a doctor"
)
async def create_doctor_router(doctor: DocterCreateSchema, db: Session = Depends(get_db)):
    return await create_doctor(db=db, doctor=doctor)


@docter_router.get(
    "/{doctor_id}",
    response_model=DoctorSchema,
    status_code=200,
    summary="Get a doctor by id",
    description="Get a doctor by id"
)
async def get_doctor_by_id_router(doctor_id: str, db: Session = Depends(get_db)):
    return await get_doctor_by_id(db=db, doctor_id=doctor_id)


@docter_router.patch(
    '/{doctor_id}',
    response_model=DoctorSchema,
    status_code=200,
    summary="Update a doctor",
    description="Update a doctor"
)
async def update_doctor_router(doctor_id: str, doctor:DoctorUpdateSchema, db: Session=Depends(get_db)):
    return await update_docter(db=db, doctor_id=doctor_id, doctor=doctor)


@docter_router.delete(
    '/{doctor_id}',
    status_code=200,
    summary="Delete a doctor",
    description="Delete a doctor"
)
async def delete_doctor_router(doctor_id: str, db: Session=Depends(get_db)):
    deleted = await delete_doctor(db, doctor_id)
    if deleted:
        return {"message": "doctor deleted successfully"}