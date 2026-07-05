from sqlalchemy.orm import Session

from app.database.models import User


def get_user(db: Session, session_id: str):
    return (
        db.query(User)
        .filter(User.session_id == session_id)
        .first()
    )


def create_user(db: Session, session_id: str):
    user = User(session_id=session_id)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)

    return user