from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.models.user_profile import UserProfile
from app.models.memory import Memory

DATABASE_URL = "sqlite:///samvaad.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()