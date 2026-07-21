import re
import requests

from app.tools.base_tool import BaseTool


class WeatherTool(BaseTool):

    @property
    def name(self):
        return "weather"

    def can_handle(self, message):

        text = message.lower()

        keywords = [
            "weather",
            "temperature",
            "forecast",
            "rain"
        ]

        return any(word in text for word in keywords)

    def execute(self, payload):

        city = payload.get("city")

        if not city:
            return "❌ City not found."

        coordinates = self.get_coordinates(city)

        if coordinates is None:
            return f"❌ Couldn't find {city}."

        latitude, longitude = coordinates

        weather = self.get_weather(latitude, longitude)

        if weather is None:
            return "❌ Unable to fetch weather."

        condition = self.get_weather_condition(
            weather["weather_code"]
        )

        recommendation = self.get_recommendation(
            weather["temperature"],
            weather["humidity"],
            weather["weather_code"]
        )

        return f"""
    🌤 Samvaad Weather Report

    📍 City : {city}

    ☁️ Condition : {condition}

    🌡 Temperature : {weather['temperature']}°C

    🥵 Feels Like : {weather['feels_like']}°C

    💧 Humidity : {weather['humidity']}%

    💨 Wind Speed : {weather['wind_speed']} km/h

    🌅 Sunrise : {weather['sunrise']}

    🌇 Sunset : {weather['sunset']}

    🤖 Recommendation

    {recommendation}
    """
    # ----------------------------------------------------

    def extract_city(self, message):

        text = message.lower()

        text = re.sub(r"[?.,!]", "", text)

        remove_words = [
            "today",
            "tomorrow",
            "now",
            "currently",
            "please"
        ]

        words = [
            word
            for word in text.split()
            if word not in remove_words
        ]

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

    # ----------------------------------------------------

    def get_coordinates(self, city):

        url = (
            "https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        if "results" not in data:
            return None

        result = data["results"][0]

        return (
            result["latitude"],
            result["longitude"]
        )

    # ----------------------------------------------------

    def get_weather(self, latitude, longitude):

        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            "&current="
            "temperature_2m,"
            "apparent_temperature,"
            "relative_humidity_2m,"
            "weather_code,"
            "wind_speed_10m"
            "&daily=sunrise,sunset"
            "&timezone=auto"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        current = data["current"]

        daily = data["daily"]

        return {

            "temperature": current["temperature_2m"],

            "feels_like": current["apparent_temperature"],

            "humidity": current["relative_humidity_2m"],

            "wind_speed": current["wind_speed_10m"],

            "weather_code": current["weather_code"],

            "sunrise": daily["sunrise"][0],

            "sunset": daily["sunset"][0]

        }

    # ----------------------------------------------------

    def get_weather_condition(self, code):

        conditions = {

            0: "☀️ Clear Sky",

            1: "🌤 Mainly Clear",

            2: "⛅ Partly Cloudy",

            3: "☁️ Overcast",

            45: "🌫 Fog",

            48: "🌫 Depositing Fog",

            51: "🌦 Light Drizzle",

            53: "🌦 Drizzle",

            55: "🌧 Heavy Drizzle",

            61: "🌧 Rain",

            63: "🌧 Moderate Rain",

            65: "🌧 Heavy Rain",

            71: "❄️ Snow",

            80: "🌦 Rain Showers",

            95: "⛈ Thunderstorm"

        }

        return conditions.get(
            code,
            "🌍 Unknown"
        )

    # ----------------------------------------------------

    def get_recommendation(
        self,
        temperature,
        humidity,
        weather_code
    ):

        if weather_code in [61, 63, 65, 80]:

            return (
                "🌧 Carry an umbrella before going outside."
            )

        if temperature >= 40:

            return (
                "🥵 Extreme heat. Stay indoors and drink plenty of water."
            )

        if temperature >= 35:

            return (
                "☀️ It's quite hot today. Stay hydrated."
            )

        if humidity >= 80:

            return (
                "💧 Humidity is high today. It may feel warmer than the actual temperature."
            )

        if weather_code == 0:

            return (
                "😎 Perfect weather for outdoor activities."
            )

        return (
            "😊 Have a wonderful day!"
        )