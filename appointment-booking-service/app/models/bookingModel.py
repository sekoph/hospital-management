from sqlalchemy import Column, Integer, Date, Boolean, UUID, DateTime, func, ForeignKey, Time
import uuid
from app.db.base import Base
from sqlalchemy.orm import relationship


class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(UUID(True), primary_key=True, default=uuid.uuid4, nullable=False)
    doctor_id = Column(UUID(True), nullable=False)
    patient_id = Column(UUID(True), nullable=False)
    appointment_date = Column(Date, nullable=False)
    appointment_start = Column(Time, nullable=False)
    appointment_end = Column(Time, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    date_created = Column(DateTime, default=func.now(), nullable=False)
    date_modified = Column(DateTime, nullable=True)