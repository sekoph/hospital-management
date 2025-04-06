from sqlalchemy import Column, String, Date, Boolean, UUID, DateTime, func, ForeignKey
import uuid
from app.db.base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(True), primary_key=True, default=uuid.uuid4, nullable=False)
    role = Column(String(100), nullable=False, default="user")
    username = Column(String(100), nullable=False, unique=True)
    hash_password = Column(String(100), nullable=False)
    date_created =  Column(DateTime, default=func.now())
    date_modified = Column(Date, nullable=True)