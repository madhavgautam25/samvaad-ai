from app.providers.ollama_provider import OllamaProvider


class AIEngine:

    def __init__(self):
        self.provider = OllamaProvider()

    def generate(self, messages):
        return self.provider.generate(messages)