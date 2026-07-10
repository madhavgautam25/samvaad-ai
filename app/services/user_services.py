from app.database.database import SessionLocal
from app.database.crud import (
    get_user,
    create_user,
    update_language,
    update_name
)


class UserService:

    def get_or_create_user(self, session_id):

        db = SessionLocal()

        user = get_user(db, session_id)

        if user is None:
            user = create_user(db, session_id)

        db.close()

        return user

    def save_language(self, session_id, language):

        db = SessionLocal()

        update_language(
            db,
            session_id,
            language
        )

        db.close()

    def save_name(self, session_id, name):

        db = SessionLocal()

        update_name(
            db,
            session_id,
            name
        )

        db.close()