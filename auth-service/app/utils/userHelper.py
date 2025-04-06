from sqlalchemy.orm import Session
from app.models.userModel import User

# helper functions to get user by username
async def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()