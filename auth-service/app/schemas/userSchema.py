from pydantic import BaseModel as Base, UUID4 , Field
from typing import Optional, Annotated, List
from datetime import datetime, date


class BaseModel(Base):
    class Config:
        protected_namespaces = ()
        
class UserSchema(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=UUID4)
    role: str
    username: str
    date_created: datetime
    date_modified: Optional[date]

    class Config:
        from_attributes = True
        
class UserCreateSchema(BaseModel):
    role: str = "user"
    username: str
    password: str
    date_created: datetime
    date_modified: date

    class Config:
        from_attributes = True
        
class UserUpdateSchema(BaseModel):
    role: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    date_modified: Optional[date] = None
    
    class config:
        from_attributes = True
        
class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "Bearer"

    class Config:
        from_attributes = True
        
class TokenDataSchema(BaseModel):
    username: Optional[str]= None
    role: Optional[str] = None

    class Config:
        from_attributes = True