from sqlalchemy import Column, String, UUID, DateTime, func
import uuid
from app.db.base import Base
from sqlalchemy.orm import relationship


class DoctorSpecialization(Base):
    __tablename__ = "doctor_specializations"

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4, nullable=False)
    specialization = Column(String(100), nullable=False)
    title = Column(String(100), nullable=True)
    description = Column(String(100), nullable=True)
    date_created =  Column(DateTime, server_default=func.now())
    date_modified = Column(DateTime, server_defaule=func.now(), onupdate=func.now())

    # Define the relationship with Doctor
    doctors = relationship("Doctor", back_populates="doctor_specializations")