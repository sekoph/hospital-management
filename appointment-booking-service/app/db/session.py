from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config.settings import settings

database_url = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(
    database_url
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = session_local()
    try:
        yield db
    finally:
        db.close()