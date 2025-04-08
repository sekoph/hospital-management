from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime, date


class BaseModel(Base):
    class Config:
        protected_namespaces = ()
        
class DoctorSchema(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=UUID4)
    specialization_id: Annotated[UUID4, str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    username: str
    phone_number: Optional[str]
    is_active: bool
    date_created: datetime
    date_modified: Optional[datetime]

    class Config:
        from_attributes = True
        
class DocterCreateSchema(BaseModel):
    specialization_id: Optional[Annotated[UUID4, str]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    username: str
    phone_number: Optional[str] = None
    is_active: Optional[bool]
    user_id: Annotated[UUID4, str]

    class Config:
        from_attributes = True
        
class DoctorUpdateSchema(BaseModel):
    specialization_id: Optional[Annotated[UUID4, str]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = None
    user_id: Optional[Annotated[UUID4, str]] = None
    
    class Config:
        from_attributes = True