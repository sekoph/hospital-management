from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime



class BaseModel(Base):
    class Config:
        protected_namespaces = ()
        
        
class DoctorSpecializationSchema(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=UUID4)
    specialization: str
    title: Optional[str]
    description: Optional[str]
    date_created: datetime
    date_modified: Optional[datetime]
    
    class Config:
        from_attributes = True

class DoctorSpecializationCreateSchema(BaseModel):
    specialization: str
    title: Optional[str]
    description: Optional[str]
    date_created: datetime
    date_modified: datetime

    class Config:
        from_attributes = True

class DoctorSpecializationUpdateSchema(BaseModel):
    specialization: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    date_modified: Optional[datetime] = None

    class Config:
        from_attributes = True
