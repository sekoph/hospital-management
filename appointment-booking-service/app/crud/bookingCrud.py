from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from app.models.bookingModel import Booking

from app.schemas.bookingSchema import (
    BookingSchema,
    BookingCreateSchema,
    BookingUpdateSchema
)

from app.utils.bookingHelper import is_doctor_available


async def get_bookings(db: Session, ) -> List[BookingSchema]:
    bookings = db.query(Booking).all()
    return [BookingSchema.from_orm(booking) for booking in bookings]

async def create_booking(db: Session, booking: BookingCreateSchema) -> BookingSchema:
    doctor_available = await is_doctor_available(db, doctor_id=booking.doctor_id,
                                        appointment_start=booking.appointment_start,
                                        appointment_end=booking.appointment_end,
                                        appointment_date=booking.appointment_date)
    if doctor_available:
        try:
            booking = Booking(**booking.dict())
            db.add(booking)
            db.commit()
            schema = BookingSchema.from_orm(booking)
            return schema
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Doctor not available at the time")

        
    
    
async def get_booking_by_id(db: Session, booking_id: str) -> BookingSchema:
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return BookingSchema.from_orm(booking)


async def update_booking(db: Session, booking_id: str, booking: BookingUpdateSchema) -> BookingSchema:
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    else:
        doctor_available = await is_doctor_available(db, doctor_id=booking.doctor_id,
                                        appointment_start=booking.appointment_start,
                                        appointment_end=booking.appointment_end,
                                        appointment_date=booking.appointment_date)
        if doctor_available:
            try:
                for key, value in booking.dict(exclude_none=True, exclude_unset=True).items():
                    setattr(db_booking, key, value)
                db.commit()
                db.refresh(db_booking)
                return BookingSchema.from_orm(db_booking)

            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update booking")
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Doctor not available at the time")

        
async def delete_booking(db: Session, booking_id: str) -> bool:
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    else:
        try:
            db.delete(db_booking)
            db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete booking")