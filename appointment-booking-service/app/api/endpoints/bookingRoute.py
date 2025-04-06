from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends

from app.db.session import get_db


from crud.bookingCrud import (
    get_bookings,
    create_booking,
    update_booking,
    get_booking_by_id,
    delete_booking
)

from schemas.bookingSchema import (
    BookingSchema,
    BookingCreateSchema,
    BookingUpdateSchema)


booking_router = APIRouter(
    prefix="/booking",
    tags=["Bookings"]
)



@booking_router.get(
    '/',
    response_model=List[BookingSchema],
    status_code=200,
    summary="Get all bookings",
    description="Get all bookings"
)
async def get_bookings_router(db: Session = Depends(get_db)):
    bookings = await get_bookings(db=db)
    return bookings


@booking_router.post(
    '/',
    response_model=BookingSchema,
    status_code=201,
    summary="Create a booking",
    description="Create a booking"
)
async def create_booking_router(
    booking: BookingCreateSchema,
    db: Session = Depends(get_db)):
    new_booking = await create_booking(db=db, booking=booking)
    return new_booking


@booking_router.patch(
    '/{booking_id}',
    response_model=BookingSchema,
    status_code=200,
    summary="Update a booking",
    description="Update a booking"
)
async def update_booking_router(
    booking_id: str,
    booking: BookingUpdateSchema,
    db: Session = Depends(get_db)):
    updated_booking = await update_booking(db=db, booking=booking, booking_id=booking_id)
    return updated_booking


@booking_router.get(
    '/{booking_id}',
    response_model=BookingSchema,
    status_code=200,
    summary="Get a booking by ID",
    description="Get a booking by ID"
)
async def get_booking_by_id_router(booking_id: str, db: Session = Depends(get_db)):
    booking = await get_booking_by_id(db=db, booking_id=booking_id)
    return booking

@booking_router.delete(
    '/{booking_id}',
    status_code=204,
    summary="Delete a booking",
    description="Delete a booking"
)
async def delete_booking_router(booking_id: str, db: Session = Depends(get_db)):
    deleted = await delete_booking(db=db, booking_id=booking_id)
    if deleted :
        return {"message": "Booking deleted successfully"}


