import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from dotenv import load_dotenv

load_dotenv()

database_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

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