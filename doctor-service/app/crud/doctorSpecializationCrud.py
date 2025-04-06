from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from app.models.doctorSpecializationModel import DoctorSpecialization

from app.schemas.doctorSpecializationSchema import (
    DoctorSpecializationCreateSchema,
    DoctorSpecializationUpdateSchema,
    DoctorSpecializationSchema)


async def get_all_doctor_specializations(db: Session) -> List[DoctorSpecializationSchema]:
    doctor_specializations = db.query(DoctorSpecialization).all()
    return [DoctorSpecializationSchema.from_orm(doctor_specialization) for doctor_specialization in doctor_specializations]


async def create_doctor_specialization(db: Session, doctor_specialization: DoctorSpecializationCreateSchema) -> DoctorSpecializationSchema:
    try:
        doctor_specialization = DoctorSpecialization(**doctor_specialization.dict())
        db.add(doctor_specialization)
        db.commit()
        schema = DoctorSpecializationSchema.from_orm(doctor_specialization)
        return schema
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
async def get_doctor_specialization_by_id(db: Session, doctor_specialization_id: str) -> DoctorSpecializationSchema:
    doctor_specialization = db.query(DoctorSpecialization).filter(DoctorSpecialization.id == doctor_specialization_id).first()
    if not doctor_specialization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor specialization not found")
    return DoctorSpecializationSchema.from_orm(doctor_specialization)


async def update_doctor_specialization(db: Session, doctor_specialization_id: str, doctor_specialization: DoctorSpecializationUpdateSchema) -> DoctorSpecializationSchema:
    specialization = db.query(DoctorSpecialization).filter(DoctorSpecialization.id == doctor_specialization_id).first()
    if not specialization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor specialization not found")
    else:
        try:
            for key, value in doctor_specialization.model_dump(exclude_none=True, exclude_unset=True).items():
                setattr(specialization, key, value)
            db.commit()
            db.refresh(specialization)
            return DoctorSpecializationSchema.from_orm(specialization)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
async def delete_doctor_specialization(db: Session, doctor_specialization_id: str) -> bool:
    doctor_specialization = db.query(DoctorSpecialization).filter(DoctorSpecialization.id == doctor_specialization_id).first()
    if not doctor_specialization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor specialization not found")
    else:
        db.delete(doctor_specialization)
        db.commit()
        return True