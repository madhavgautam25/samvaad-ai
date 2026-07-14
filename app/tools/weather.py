import re
import requests

from app.tools.base_tool import BaseTool


class WeatherTool(BaseTool):

    @property
    def name(self):
        return "weather"

    def can_handle(self, message):

        text = message.lower()

        return "weather" in text

    def execute(self, message):

        city = self.extract_city(message)

        if city is None:
            return "Please tell me the city."

        return f"🌤 Weather tool detected city: {city.title()}"

    def extract_city(self, message):


        text = message.lower()

        # Remove punctuation
        text = re.sub(r"[?.,!]", "", text)

        # Remove common filler words
        remove_words = [
            "today",
            "tomorrow",
            "now",
            "currently",
            "please"
        ]

        words = text.split()

        words = [word for word in words if word not in remove_words]

        text = " ".join(words)

        patterns = [

            r"weather in ([a-zA-Z ]+)",

            r"temperature in ([a-zA-Z ]+)",

            r"forecast for ([a-zA-Z ]+)",

            r"weather ([a-zA-Z ]+)"
        ]

        for pattern in patterns:

            match = re.search(pattern, text)

            if match:

                return match.group(1).strip()

        return None