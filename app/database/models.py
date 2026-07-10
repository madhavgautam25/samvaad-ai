from sqlalchemy import Column, String

from app.database.database import Base


class User(Base):

    __tablename__ = "users"

    session_id = Column(String, primary_key=True, index=True)

    name = Column(String, nullable=True)

    language = Column(String, nullable=True)

    city = Column(String, nullable=True)

    profession = Column(String, nullable=True)