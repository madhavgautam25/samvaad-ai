from app.services.ai_engine import AIEngine
from app.memory.memory_manager import MemoryManager
from app.models.user_profile import UserProfile
from app.core.prompt_builder import PromptBuilder
from app.services.user_services import UserService
from app.core.profile_manager import ProfileManager
from app.tools.tool_router import ToolRouter

class ConversationEngine:

    def __init__(self):
        self.ai = AIEngine()
        self.memory = MemoryManager()
        self.profile = UserProfile()
        self.user_service = UserService()
        self.tool_router = ToolRouter()

    def chat(self, session_id, user_message):

        # -----------------------------------
        # Language Selection
        # -----------------------------------

        if self.profile.language is None:

            language = user_message.strip().lower()

            if language in ["english", "en"]:

                self.profile.language = "English"

                self.user_service.save_language(
                    session_id,
                    "English"
                )

                return (
                    "✅ English selected!\n\n"
                    "Hello! 👋\n"
                    "I'm Samvaad AI, created by Madhav Gautam.\n"
                    "How can I help you today?"
                )

            elif language in ["hindi", "hi", "हिन्दी", "हिंदी"]:

                self.profile.language = "Hindi"

                self.user_service.save_language(
                    session_id,
                    "Hindi"
                )

                return (
                    "✅ हिन्दी चुनी गई।\n\n"
                    "नमस्ते! 👋\n"
                    "मैं Samvaad AI हूँ।\n"
                    "आज मैं आपकी किस प्रकार सहायता कर सकता हूँ?"
                )

            elif language in ["punjabi", "pa", "ਪੰਜਾਬੀ"]:

                self.profile.language = "Punjabi"

                self.user_service.save_language(
                    session_id,
                    "Punjabi"
                )

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
        # Name Extraction
        # -----------------------------------

        extracted_name = ProfileManager.extract_name(user_message)

        if extracted_name:

            self.profile.name = extracted_name

            self.user_service.save_name(
                session_id,
                extracted_name
            )

        # -----------------------------------
        # Quick Profile Questions
        # -----------------------------------

        if user_message.lower() in [
            "what's my name?",
            "what is my name?",
            "who am i?"
        ]:

            if self.profile.name:
                return f"Your name is {self.profile.name}."

            return "I don't know your name yet."

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
        
        tool_response = self.tool_router.handle(user_message)

        if tool_response:
            return tool_response

        response = self.ai.generate(messages)

        self.memory.add(
            "assistant",
            response
        )

        return response