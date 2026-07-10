from app.tools.weather import WeatherTool


class ToolRouter:

    def __init__(self):

        self.weather = WeatherTool()

    def handle(self, message):

        text = message.lower()

        if "weather" in text:

            words = text.split()

            city = words[-1]

            return self.weather.get_weather(city)

        return None