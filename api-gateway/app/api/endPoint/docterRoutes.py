from fastapi import FastAPI, status, Request, Response, Depends
from fastapi.routing import APIRouter

from app.config import settings
from app.core.customizedRouter import route

# from app.api.endPoint.server import app

from app.schemas.doctorSchema import (
    DocterCreateSchema,
    DoctorUpdateSchema,
)


from app.schemas.doctorSpecializationSchema import (
    DoctorSpecializationCreateSchema,
    DoctorSpecializationUpdateSchema
)

app = APIRouter()

# doctor routes
@route(
    request_method=app.get,
    path="/doctors",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    response_model='app.schemas.doctorSchema.DoctorSchema',
    response_list=True
)
async def get_doctors(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/doctors/{doctor_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSchema.DoctorSchema'
)
async def get_doctor(request: Request, response: Response, doctor_id: str):
    pass

@route(
    request_method=app.patch,
    path="/doctors/{doctor_id}",
    status_code=status.HTTP_201_CREATED,
    payload_key="doctor",
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSchema.DoctorSchema'
)
async def update_doctor(request: Request, response: Response, doctor_id: str, doctor: DoctorUpdateSchema):
    pass

@route(
    request_method=app.post,
    path="/doctors",
    status_code=status.HTTP_201_CREATED,
    payload_key="doctor",
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSchema.DoctorSchema'
)
async def create_doctor(request: Request, response: Response, doctor: DocterCreateSchema):
    pass


@route(
    request_method=app.delete,
    path="/doctors/{doctor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    # response_model="app.schemas.DoctorSchema"
)
async def delete_doctor(request: Request, response: Response, doctor_id: str):
    pass

# doctor_speciality routes
@route(
    request_method=app.get,
    path="/doctor_specialization",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSpecializationSchema.DoctorSpecializationSchema',
    response_list=True
)
async def get_doctor_specialities(request: Request, response: Response):
    pass

@route(
    request_method=app.get,
    path="/doctor_specialization/{doctor_specialization_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSpecializationSchema.DoctorSpecializationSchema'
)
async def get_doctor_speciality(request: Request, response: Response, doctor_specialization_id: str):
    pass


@route(
    request_method=app.patch,
    path="/doctor_specialization/{doctor_specialization_id}",
    status_code=status.HTTP_201_CREATED,
    payload_key="doctor_specialization",
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSpecializationSchema.DoctorSpecializationSchema'
)
async def update_doctor_speciality(request: Request, response: Response, doctor_specialization_id: str, doctor_specialization: DoctorSpecializationUpdateSchema):
    pass

@route(
    request_method=app.post,
    path="/doctor_specialization",
    status_code=status.HTTP_201_CREATED,
    payload_key="doctor_specialization",
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.doctorSpecializationSchema.DoctorSpecializationSchema'
)
async def create_doctor_speciality(request: Request, response: Response, doctor_specialization: DoctorSpecializationCreateSchema):
    pass

@route(
    request_method=app.delete,
    path="/doctor_specialization/{doctor_specialization_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.DOCTOR_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    # response_model="app.schemas.DoctorSpecializationSchema"
)
async def delete_doctor_speciality(request: Request, response: Response, doctor_specialization_id: str):
    pass

