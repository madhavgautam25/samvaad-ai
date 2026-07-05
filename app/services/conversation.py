from app.services.ai_engine import AIEngine
from app.memory.memory_manager import MemoryManager
from app.core.personality import SYSTEM_PROMPT


class ConversationEngine:

    def __init__(self):
        self.ai = AIEngine()
        self.memory = MemoryManager()

    def chat(self, user_message):

        if not self.memory.get_messages():

            self.memory.add(
                "system",
                SYSTEM_PROMPT
            )

        self.memory.add(
            "user",
            user_message
        )

        response = self.ai.generate(
            self.memory.get_messages()
        )

        self.memory.add(
            "assistant",
            response
        )

        return response