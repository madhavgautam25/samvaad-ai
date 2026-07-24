from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String,
        index=True,
        nullable=False
    )

    key = Column(
        String,
        nullable=False
    )

    value = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )