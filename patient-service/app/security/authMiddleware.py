from fastapi import Depends, HTTPException, status, Request
from app.config.settings import settings
import fastapi.security as _security
from jose import jwt, JWTError
import httpx


oauth2_scheme = _security.OAuth2PasswordBearer(settings.TOKEN_URL)

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def get_current_user(token: str = Depends(oauth2_scheme)):
    # print("extracted token",token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # print("decoding token")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print("payload")
        username: str = payload.get("sub")
        role: str = payload.get("role")
        # print(username, role)

        if username is None or role is None:
            raise credentials_exception
        return {"username": username, "role": role}
    except JWTError:
        raise credentials_exception



# headers = {
#     "Content-Type": "application/json"
# }

# async def get_current_user():
#     async with httpx.AsyncClient() as client:
#         response = await client.get(settings.TOKEN_URL, headers=headers)
#         if response.status_code == 200:
#             return response.json()  # Make sure you're returning the user data
#         raise HTTPException(status_code=401, detail="Not authenticated")
