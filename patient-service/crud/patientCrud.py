import uuid
from typing import List, Union, Optional
from sqlalchemy.orm import Session
from models.patientModel import Patient

from fastapi import HTTPException

from starlette import status

from schemas.patientSchema import (
    PatientCreateSchema,
    PatientUpdateSchema,
    PatientSchema)


async def get_all_patients(db: Session) -> List[PatientSchema]:
    patients = db.query(Patient).all()
    return [PatientSchema.from_orm(patient) for patient in patients]


async def create_patient(db: Session, patient: PatientCreateSchema) -> PatientSchema:
    try:
        patient = Patient(**patient.dict())
        db.add(patient)
        db.commit()
        schema = PatientSchema.from_orm(patient)
        return schema
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create a patient")
    
    
async def get_patient_by_id(db: Session, patient_id: str) -> PatientSchema:
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return PatientSchema.from_orm(patient)


async def update_patient(db: Session, patient_id: str, patient: PatientUpdateSchema) -> PatientSchema:
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    else:
        try:
            for key, value in patient.dict(exclude_none=True, exclude_unset=True).items():
                setattr(db_patient, key, value)
            db.commit()
            db.refresh(db_patient)
            return PatientSchema.from_orm(db_patient)
            
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update patient")
    

async def delete_patient(db: Session, patient_id: str) -> bool:
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    else:
        try:
            db.delete(patient)
            db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete patient")