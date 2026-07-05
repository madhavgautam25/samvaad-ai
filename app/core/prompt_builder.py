from app.core.personality import SYSTEM_PROMPT


class PromptBuilder:

    @staticmethod
    def build(memory_messages):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(memory_messages)

        return messages