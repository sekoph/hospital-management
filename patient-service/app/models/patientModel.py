from sqlalchemy import Column, String, Date, Boolean, UUID, DateTime, func
import uuid
from sqlalchemy.orm import relationship

from app.db.base import Base




class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(UUID(True), primary_key=True, default=uuid.uuid4, nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    username= Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(100), nullable=True, unique=True)
    date_of_birth = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    date_created =  Column(DateTime, server_default=func.now())
    date_modified = Column(Date, server_default=func.now(), onupdate=func.now())
    user_id = Column(UUID(True), nullable=False)
    
    # Define the relationship with PatientInsurance
    patient_insurance = relationship("PatientInsurance", back_populates="patients" , uselist=False)
    
    
    