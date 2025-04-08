from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.models.userModel import User
from app.utils.userHelper import get_user_by_username

from app.security.auth import (
    get_password_hash,
    authenticate_user,
    create_access_token,
    get_current_user)

from app.db.session import get_db


from app.crud.userCrud import (
    get_all_users,
    create_user,
    update_user,
    delete_user,
)

from app.schemas.userSchema import (
    UserSchema,
    UserCreateSchema,
    TokenSchema,
    TokenDataSchema,
    userLoginSchema,
    UserUpdateSchema
)

from app.config.settings import settings

from app.kafka.producer.userProducer import UserProducer



ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


user_router = APIRouter(
    prefix="/auth",
    tags=["Users endpoints"]
)

async def get_kafka_producer():
    producer = UserProducer(bootstrap_servers=settings.bootstrap_servers)
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()

@user_router.post(
    "/register_user",
    response_model=UserSchema,
    status_code=201,
    summary="Create a user",
    description="Create a user"
)
async def create_user_router(user: UserCreateSchema, producer: UserProducer = Depends(get_kafka_producer) ,db: Session = Depends(get_db)):
    # db_user = db.query(User).filter(User.username == user.username).first()
    db_user = await get_user_by_username(db, user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    return await create_user(db=db, user=user)


@user_router.post(
    '/login',
    response_model=TokenSchema,
    status_code=200,
    summary="Login a user",
    description="Login a user"
)
async def login_user_router(form_data: userLoginSchema, db: Session = Depends(get_db)):
    user = await authenticate_user(db,form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    # subject = user.username + user.role
    access_token = await create_access_token(
        data={"sub": user.username, "role": user.role, "id": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@user_router.get(
    "/me",
    response_model=TokenDataSchema,
    status_code=200,
    summary="get catch logged in user",
    description="Get catch logged in user"
)
async def read_logged_in_user(current_user: User = Depends(get_current_user)):
    try:
        return current_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    
@user_router.get(
    "/users",
    response_model=List[UserSchema],
    status_code=200,
    summary="Get all users",
    description="Get all users"
)
async def get_users(db: Session = Depends(get_db)):
    return await get_all_users(db)


@user_router.patch(
    "/users/{user_id}",
    response_model=UserSchema,
    status_code=200,
    summary="Update a user",
    description="Update a user"
)
async def update_user_router(user_id: str, user: UserUpdateSchema, db: Session = Depends(get_db)):
    return await update_user(db, user_id, user)

@user_router.delete(
    "/users/{user_id}",
    status_code=200,
    summary="Delete a user",
    description="Delete a user"
)
async def delete_user_router(user_id: str, db: Session = Depends(get_db)):
    deleted_user = await delete_user(user_id=user_id, db=db)
    if deleted_user:
        return {"message" : "User deleted successfully"}