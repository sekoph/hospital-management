from sqlalchemy import Column, String, Date, Boolean, UUID, DateTime, func, ForeignKey
import uuid
from app.db.base import Base
from sqlalchemy.orm import relationship


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4, nullable=False)
    specialization_id = Column(UUID(True), ForeignKey("doctor_specializations.id", ondelete="CASCADE"), nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(100), nullable=True, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    date_created =  Column(DateTime, server_default=func.now())
    date_modified = Column(DateTime, server_default=func.now(), onupdate=func.now())
    user_id = Column(UUID(True),nullable=False)

    # Define the relationship with Doctor
    doctor_specializations = relationship("DoctorSpecialization", back_populates="doctors")