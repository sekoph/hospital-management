import uuid
from typing import List, Union, Optional
from sqlalchemy.orm import Session
from models.patientInsuranceModel import PatientInsurance
from fastapi import HTTPException
from starlette import status

from schemas.patientInsuranceSchema import (
    PatientInsuranceCreateSchema,
    PatientInsuranceUpdateSchema,
    PatientInsuranceSchema)


async def get_all_patients_insurances(db: Session) -> List[PatientInsuranceSchema]:
    patient_insurances = db.query(PatientInsurance).all()
    return [PatientInsuranceSchema.from_orm(patient_insurance) for patient_insurance in patient_insurances]



async def create_patient_insurance(db: Session, patient_insurance: PatientInsuranceCreateSchema) -> PatientInsuranceSchema:
    try:
        patient_insurance = PatientInsurance(**patient_insurance.dict())
        db.add(patient_insurance)
        db.commit()
        schema = PatientInsuranceSchema.from_orm(patient_insurance)
        return schema
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
async def get_insurance_info_by_patient_id(db: Session, patient_id: str) -> PatientInsuranceSchema:
    patient_insurance = db.query(PatientInsurance).filter(PatientInsurance.patient_id == patient_id).first()
    if not patient_insurance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient insurance not found")
    return PatientInsuranceSchema.from_orm(patient_insurance)


async def update_patient_insurance_info(db: Session, patient_id: str, patient_insurance: PatientInsuranceUpdateSchema) -> PatientInsuranceSchema:
    db_patient_insurance = db.query(PatientInsurance).filter(PatientInsurance.patient_id == patient_id).first()
    if not db_patient_insurance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient insurance not found")
    else:
        try:
            for key, value in patient_insurance.dict(exclude_none=True, exclude_unset=True).items():
                setattr(db_patient_insurance, key, value)
            db.commit()
            db.refresh(db_patient_insurance)
            return PatientInsuranceSchema.from_orm(db_patient_insurance)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update patient insurance")
        
        


async def delete_patient_insurance_info(db: Session, patient_id: str) -> bool:
    patient_insurance = db.query(PatientInsurance).filter(PatientInsurance.patient_id == patient_id).first()
    if not patient_insurance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient insurance not found")
    else:
        db.delete(patient_insurance)
        db.commit()
        return True