from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from app.models.doctorModel import Doctor


from app.schemas.doctorSchema import(
        DoctorSchema,
        DocterCreateSchema,
        DoctorUpdateSchema
        )


async def get_all_doctors(db: Session) -> List[DoctorSchema]:
    doctors = db.query(Doctor).all()
    return [DoctorSchema.from_orm(doctor) for doctor in doctors]


async def create_doctor(db: Session, doctor: DocterCreateSchema) -> DoctorSchema:
    try:
        doctor = Doctor(**doctor.dict())
        db.add(doctor)
        db.commit()
        schema = DoctorSchema.from_orm(doctor)
        return schema
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_doctor_by_id(db: Session, doctor_id: str) -> DoctorSchema:
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    return DoctorSchema.from_orm(doctor)


async def update_docter(db: Session, doctor_id: str, doctor: DoctorUpdateSchema) -> DoctorSchema:
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not db_doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    else:
        try:
            for key, value in doctor.model_dump(exclude_none=True, exclude_unset=True).items():
                setattr(db_doctor, key, value)
            db.commit()
            db.refresh(db_doctor)
            return DoctorSchema.from_orm(db_doctor)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        
async def delete_doctor(db: Session, doctor_id: str) -> bool:
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    else:
        db.delete(doctor)
        db.commit()
        return True
