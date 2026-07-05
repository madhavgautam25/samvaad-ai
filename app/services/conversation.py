from app.services.ai_engine import AIEngine
from app.memory.memory_manager import MemoryManager
from app.models.user_profile import UserProfile
from app.core.prompt_builder import PromptBuilder


class ConversationEngine:

    def __init__(self):
        self.ai = AIEngine()
        self.memory = MemoryManager()
        self.profile = UserProfile()

    def chat(self, user_message):

        # -----------------------------------
        # Language Selection
        # -----------------------------------

        if self.profile.language is None:

            language = user_message.strip().lower()

            if language in ["english", "en"]:

                self.profile.language = "English"

                return (
                    "✅ English selected!\n\n"
                    "Hello! 👋\n"
                    "I'm Samvaad AI, created by Madhav Gautam.\n"
                    "How can I help you today?"
                )

            elif language in ["hindi", "hi", "हिन्दी", "हिंदी"]:

                self.profile.language = "Hindi"

                return (
                    "✅ हिन्दी चुनी गई।\n\n"
                    "नमस्ते! 👋\n"
                    "मैं Samvaad AI हूँ।\n"
                    "आज मैं आपकी किस प्रकार सहायता कर सकता हूँ?"
                )

            elif language in ["punjabi", "pa", "ਪੰਜਾਬੀ"]:

                self.profile.language = "Punjabi"

                return (
                    "✅ ਪੰਜਾਬੀ ਚੁਣੀ ਗਈ।\n\n"
                    "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! 👋\n"
                    "ਮੈਂ Samvaad AI ਹਾਂ।\n"
                    "ਅੱਜ ਮੈਂ ਤੁਹਾਡੀ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?"
                )

            else:

                return (
                    "👋 Welcome to Samvaad AI!\n\n"
                    "Before we start, please choose your preferred language.\n\n"
                    "1. English\n"
                    "2. Hindi\n"
                    "3. Punjabi\n\n"
                    "Simply type: English, Hindi or Punjabi."
                )

        # -----------------------------------
        # Normal Conversation
        # -----------------------------------

        self.memory.add(
            "user",
            user_message
        )

        messages = PromptBuilder.build(
            self.memory.get_messages()
        )

        response = self.ai.generate(messages)

        self.memory.add(
            "assistant",
            response
        )

        return response