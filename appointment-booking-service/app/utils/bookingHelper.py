from datetime import datetime, timedelta, date, time
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from fastapi import HTTPException
from app.models.bookingModel import Booking



async def is_doctor_available(db, doctor_id: str,
                            appointment_date: date,
                            appointment_start: time,
                            appointment_end: time) -> bool:
    
    # Doctor unavailable time - create naive time objects
    unavailable_start = datetime.strptime("18:00", "%H:%M").time()
    unavailable_end = datetime.strptime("19:00", "%H:%M").time()
    
    # Ensure appointment_start is also naive (no timezone info)
    if hasattr(appointment_start, 'tzinfo') and appointment_start.tzinfo is not None:
        # Convert aware time to naive time if needed
        # This is one approach - alternatively you could make all times timezone-aware
        appointment_start = appointment_start.replace(tzinfo=None)
    
    if hasattr(appointment_end, 'tzinfo') and appointment_end.tzinfo is not None:
        appointment_end = appointment_end.replace(tzinfo=None)
    
    if unavailable_start <= appointment_start < unavailable_end:
        return False
    
    overlapping_booking = (
        db.query(Booking)
        .filter(
            Booking.doctor_id == doctor_id,
            Booking.appointment_date == appointment_date,  # Ensure same date
            Booking.is_active == True,  # Only check active bookings
            Booking.appointment_start < appointment_end,  # New appointment overlaps
            Booking.appointment_end > appointment_start  # New appointment overlaps
        )
        .first()
    )
    
    if overlapping_booking:
        return False
    
    return True
    
    