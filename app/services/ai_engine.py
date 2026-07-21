from app.providers.ollama_provider import OllamaProvider


class AIEngine:

    def __init__(self):
        self.provider = OllamaProvider()

    def generate(self, data):

        # If a plain string prompt is provided,
        # convert it into Ollama's expected message format.
        if isinstance(data, str):

            messages = [
                {
                    "role": "user",
                    "content": data
                }
            ]

        else:
            messages = data

        return self.provider.generate(messages)