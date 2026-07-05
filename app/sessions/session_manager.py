from app.services.conversation import ConversationEngine


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def get_engine(self, session_id: str):

        if session_id not in self.sessions:
            self.sessions[session_id] = ConversationEngine()

        return self.sessions[session_id]