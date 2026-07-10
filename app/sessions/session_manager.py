from app.services.conversation import ConversationEngine
from app.models.user_profile import UserProfile
from app.services.user_services import UserService


class SessionManager:

    def __init__(self):
        self.sessions = {}
        self.user_service = UserService()

    def get_engine(self, session_id):

        if session_id not in self.sessions:

            user = self.user_service.get_or_create_user(session_id)

            profile = UserProfile(
                name=user.name,
                language=user.language
            )

            engine = ConversationEngine()
            engine.profile = profile

            self.sessions[session_id] = engine

        return self.sessions[session_id]