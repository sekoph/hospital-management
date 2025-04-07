from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError, JWTError

from datetime import datetime, timedelta

from app.config import settings
from app.utils.exceptions import AuthTokenMissing, AuthTokenExpired, AuthTokenCorrupted


def generate_access_token(
        data: dict,
        expires_delta: timedelta = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
):

    expire = datetime.utcnow() + expires_delta
    token_data = {
        'id': data['id'],
        'user_type': data['user_type'],
        'exp': expire,
    }

    encoded_jwt = jwt.encode(token_data, SECRET_KEY=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt



def decode_access_token(authorization: str = None):
    if not authorization:
        raise AuthTokenMissing('Auth token is missing in headers.')

    token = authorization.replace('Bearer ', '')
    try:
        payload = jwt.decode(token,settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        print(payload.get("role"))
        return payload
    except ExpiredSignatureError:
        raise AuthTokenExpired('Auth token is expired.')
    except JWTError:
        raise AuthTokenCorrupted('Auth token is corrupted.')
        


def generate_request_header(token_payload):
    return {'request-user-id': str(token_payload['id'])}


def is_admin_user(token_payload):
    return token_payload['role'] == 'admin'


def is_default_user(token_payload):
    return token_payload['role'] == 'user'

def is_doctor_user(token_payload):
    return token_payload['role'] == 'doctor'