from sqlalchemy import Column,String, Date, Boolean, UUID, ForeignKey, DateTime, func
import uuid
from utils.db import Base
from sqlalchemy.orm import relationship



class PatientInsurance(Base):
    __tablename__ = "patient_insurance"

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4, nullable=False)
    patient_id = Column(UUID(True), ForeignKey("patients.id", ondelete="CASCADE"), nullable=False, unique=True)
    provider_name = Column(String(100), nullable=False)
    policy_number = Column(String(100), nullable=False, unique=True)
    group_number = Column(String(100), nullable=True)
    plan_type = Column(String(100), nullable=True)
    coverage_start_date = Column(Date, nullable=True)
    coverage_end_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    date_created =  Column(DateTime, default=func.now())
    date_modified = Column(DateTime, nullable=True)
    
    # Define the relationship with Patient
    patients = relationship("Patient", back_populates="patient_insurance")