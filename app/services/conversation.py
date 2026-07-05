from app.services.ai_engine import AIEngine
from app.core.personality import SYSTEM_PROMPT


class ConversationEngine:

    def __init__(self):
        self.ai = AIEngine()

    def chat(self, message):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ]

        return self.ai.generate(messages)