from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime, date


class BaseModel(Base):
    class Config:
        protected_namespaces = ()


class Patient(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=UUID4)
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    username: str
    phone_number: Optional[str]
    date_of_birth: Optional[date]
    is_active: bool
    date_created: datetime
    date_modified: Optional[date]
    
    class Config:
        from_attributes = True
    
class PatientCreateSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    phone_number: str
    date_of_birth: datetime
    is_active: Optional[bool]
    date_created: datetime
    date_modified: datetime
    
    class Config:
        from_attributes = True


class PatientUpdateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    is_active: Optional[bool] = None
    # date_created: datetime
    date_modified: Optional[date] = None

    class Config:
        from_attributes = True
