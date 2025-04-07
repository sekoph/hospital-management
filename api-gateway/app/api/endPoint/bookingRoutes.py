from fastapi import FastAPI, status, Request, Response, Depends
from fastapi.routing import APIRouter
from app.config import settings
from app.core.customizedRouter import route



from app.schemas.bookingSchema import (
    BookingCreateSchema,
    BookingUpdateSchema)

# # from app.api.endPoint.server import app

app = APIRouter()

# appointment routes
@route(
    request_method=app.get,
    path="/booking",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.APPOINTMENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.bookingSchema.BookingSchema',
    response_list=True
)
async def get_appointments(request: Request, response: Response):
    pass

@route(
    request_method=app.get,
    path="/booking/{booking_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.APPOINTMENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.bookingSchema.BookingSchema'
)
async def get_appointment(request: Request, response: Response, booking_id: str):
    pass


@route(
    request_method=app.post,
    path="/booking",
    status_code=status.HTTP_201_CREATED,
    payload_key="booking",
    service_url=settings.APPOINTMENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.bookingSchema.BookingSchema'
)
async def create_appointment(request: Request, response: Response, booking: BookingCreateSchema):
    pass

@route(
    request_method=app.patch,
    path="/booking/{booking_id}",
    status_code=status.HTTP_201_CREATED,
    payload_key="booking",
    service_url=settings.APPOINTMENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.bookingSchema.BookingSchema'
)
async def update_appointment(request: Request, response: Response, booking_id: str, booking: BookingUpdateSchema):
    pass

@route(
    request_method=app.delete,
    path="/booking/{booking_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.APPOINTMENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    # response_model="app.schemas.BookingSchema"
)
async def delete_appointment(request: Request, response: Response, booking_id: str):
    pass