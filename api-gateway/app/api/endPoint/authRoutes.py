from fastapi import  status, Request, Response, Depends
from fastapi.routing import APIRouter
from app.config import settings
from app.core.customizedRouter import route
from fastapi.security import OAuth2PasswordRequestForm

# from app.api.endPoint.server import app
app = APIRouter()

from app.schemas.userSchema import (
    UserCreateSchema,
    userLoginSchema
)




@route(
    request_method=app.post,
    path="/auth/login",
    status_code=status.HTTP_200_OK,
    payload_key="form_data",
    service_url=settings.AUTH_SERVICE_URL,
    authentication_required=False,
    post_processing_func=None,
    response_model="app.schemas.userSchema.TokenSchema"
)
async def login(request: Request, response: Response,form_data: userLoginSchema):
    pass


@route(
    request_method=app.post,
    path="/auth/register_user",
    status_code=status.HTTP_201_CREATED,
    payload_key="user",
    service_url=settings.AUTH_SERVICE_URL,
    authentication_required=False,
    post_processing_func=None,
    response_model="app.schemas.userSchema.UserSchema"
)
async def register(request: Request, response: Response, user: UserCreateSchema):
    pass



