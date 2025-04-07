from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime, date


class BaseModel(Base):
    class Config:
        protected_namespaces = ()
        
class PatientInsuranceSchema(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=UUID4)
    patient_id: Annotated[UUID4, str]
    provider_name: str
    policy_number: str
    group_number: Optional[str]
    plan_type: Optional[str]
    coverage_start_date: Optional[date]
    coverage_end_date: Optional[date]
    is_active: bool
    date_created: datetime
    date_modified: Optional[datetime]

    class Config:
        from_attributes = True
        
class PatientInsuranceCreateSchema(BaseModel):
    patient_id: Annotated[UUID4, str]
    provider_name: str
    policy_number: str
    group_number: Optional[str]
    plan_type: Optional[str]
    coverage_start_date: Optional[date]
    coverage_end_date: Optional[date]
    is_active: Optional[bool]
    date_created: datetime
    date_modified: Optional[datetime]
    
    class Config:
        from_attributes = True
        
        
class PatientInsuranceUpdateSchema(BaseModel):
    patient_id: Optional[Annotated[UUID4, str]] = None
    provider_name: Optional[str] = None
    policy_number: Optional[str] = None
    group_number: Optional[str] = None
    plan_type: Optional[str] = None
    coverage_start_date: Optional[date] = None
    coverage_end_date: Optional[date] = None
    is_active: Optional[bool] = None
    date_modified: Optional[datetime] = None
    
    class Config:
        from_attributes = True