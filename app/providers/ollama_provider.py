from ollama import chat
from app.core.config import settings


class OllamaProvider:

    def generate(self, messages):
        response = chat(
            model=settings.MODEL_NAME,
            messages=messages
        )

        return response["message"]["content"]