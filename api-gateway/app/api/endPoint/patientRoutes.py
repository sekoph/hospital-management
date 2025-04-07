from fastapi import FastAPI, status, Request, Response
from fastapi.routing import APIRouter
from app.config import settings
from app.core.customizedRouter import route


# from app.api.endPoint.server import app


from app.schemas.patientInsuranceSchema import (
    PatientInsuranceCreateSchema,
    PatientInsuranceUpdateSchema
)

from app.schemas.patientSchema import (
    PatientCreateSchema,
    PatientUpdateSchema,
    
)

app = APIRouter()


# patient routes
@route(
    request_method=app.get,
    path="/patient",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    response_model='app.schemas.patientSchema.Patient',
    response_list=True
)
async def get_patients(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path="/patient/{patient_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.patientSchema.Patient'
)
async def get_patient(request: Request, response: Response, patient_id: str):
    pass


@route(
    request_method=app.patch,
    path="/patient/{patient_id}",
    status_code=status.HTTP_201_CREATED,
    payload_key="patient",
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.patientSchema.Patient'
)
async def update_patient(request: Request, response: Response, patient_id: str, patient: PatientUpdateSchema):
    pass


@route(
    request_method=app.post,
    path="/patient",
    status_code=status.HTTP_201_CREATED,
    payload_key="patient",
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.patientSchema.Patient'
)
async def create_patient(request: Request, response: Response, patient: PatientCreateSchema):
    pass


@route(
    request_method=app.delete,
    path="/patient/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    # response_model=None
)
async def delete_patient(request: Request, response: Response, patient_id: str):
    pass


# patient insurance routes
@route(
    request_method=app.get,
    path="/patient_insurances",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_admin_user',
    response_model='app.schemas.patientSchema.Patient',
    response_list=True
)
async def get_patient_insurances(request: Request, response: Response):
    pass

@route(
    request_method=app.get,
    path="/patient_insurances/{patient_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.patientInsuranceSchema.PatientInsuranceSchema'
)
async def get_patient_insurance(request: Request, response: Response, patient_id: str):
    pass

@route(
    request_method=app.patch,
    path="/patient_insurances/{patient_id}",
    status_code=status.HTTP_201_CREATED,
    payload_key="patient_insurance",
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.patientInsuranceSchema.PatientInsuranceSchema'
)
async def update_patient_insurance(request: Request, response: Response, patient_id: str, patient_insurance: PatientInsuranceUpdateSchema):
    pass

@route(
    request_method=app.post,
    path="/patient_insurances",
    status_code=status.HTTP_201_CREATED,
    payload_key="patient_insurance",
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    response_model='app.schemas.patientInsuranceSchema.PatientInsuranceSchema'
)
async def create_patient_insurance(request: Request, response: Response, patient_insurance: PatientInsuranceCreateSchema):
    pass

@route(
    request_method=app.delete,
    path="/patient_insurances/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    payload_key=None,
    service_url=settings.PATIENT_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='app.core.auth.decode_access_token',
    service_authorization_checker='app.core.auth.is_default_user',
    # response_model="app.schemas.PatientInsuranceSchema"
)
async def delete_patient_insurance(request: Request, response: Response, patient_id: str):
    pass

