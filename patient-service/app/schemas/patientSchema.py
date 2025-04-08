from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime, date


class BaseModel(Base):
    class Config:
        protected_namespaces = ()


class PatientSchema(BaseModel):
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
    user_id: Annotated[UUID4, str]
    
    class Config:
        from_attributes = True
    
class PatientCreateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    username: str
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    is_active: Optional[bool]
    # date_created: datetime
    # date_modified: datetime
    user_id: Annotated[UUID4, str]
    
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
    # date_modified: Optional[date] = None
    user_id: Optional[Annotated[UUID4, str]] = None

    class Config:
        from_attributes = True
