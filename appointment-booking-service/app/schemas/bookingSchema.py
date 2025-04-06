from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime, date, time


class BaseModel(Base):
    class Config:
        protected_namespaces = ()
        
class BookingSchema(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=UUID4)
    doctor_id: Annotated[UUID4, str]
    patient_id: Annotated[UUID4, str]
    appointment_date: date
    appointment_start: time
    appointment_end: time
    is_active: bool
    date_created: datetime
    date_modified: Optional[datetime]
    
    
    class Config:
        from_attributes = True
        
class BookingCreateSchema(BaseModel):
    doctor_id: Annotated[UUID4, str]
    patient_id: Annotated[UUID4, str]
    appointment_date: date
    appointment_start: time
    appointment_end: time
    is_active: Optional[bool]
    date_created: datetime
    date_modified: Optional[datetime]

    class Config:
        from_attributes = True
        
        
class BookingUpdateSchema(BaseModel):
    doctor_id: Optional[Annotated[UUID4, str]] = None
    patient_id: Optional[Annotated[UUID4, str]] = None
    appointment_date: Optional[date] = None
    appointment_start: Optional[time] = None
    appointment_end: Optional[time] = None
    is_active: Optional[bool] = None
    date_modified: Optional[datetime] = None