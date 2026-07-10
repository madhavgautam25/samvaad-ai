import json

from ollama import chat

from app.core.config import settings


class ProfileExtractor:

    def extract(self, message):

        response = chat(

            model=settings.MODEL_NAME,

            messages=[

                {
                    "role": "system",
                    "content": """
Extract user information.

Return ONLY JSON.

Fields:

name

city

profession

If unknown use null.

Example:

{
"name":"Madhav",
"city":"Patiala",
"profession":"Student"
}
"""
                },

                {
                    "role": "user",
                    "content": message
                }

            ]

        )

        try:

            return json.loads(
                response["message"]["content"]
            )

        except:

            return {}