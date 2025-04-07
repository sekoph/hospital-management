from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from app.models.userModel import User

from app.schemas.userSchema import (
    UserCreateSchema,
    UserUpdateSchema,
    UserSchema)


async def get_all_users(db: Session) -> List[UserSchema]:
    users = db.query(User).all()
    return [UserSchema.from_orm(user) for user in users]


async def create_user(db: Session, user: UserCreateSchema) -> UserSchema:
    try:
        user = User(username = user.username, hash_password=user.password, role=user.role)
        db.add(user)
        db.commit()
        schema = UserSchema.from_orm(user)
        return schema
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
    
async def get_user_by_username(db: Session, username: str) -> UserSchema:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserSchema.from_orm(user)


async def update_user(db: Session, user_id: str, user: UserUpdateSchema) -> UserSchema:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    else:
        try:
            for key, value in user.dict(exclude_none=True, exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
            return UserSchema.from_orm(db_user)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update user")
        
        
async def delete_user(db: Session, user_id: str) -> bool:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    else:
        try:
            db.delete(db_user)
            db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete user")