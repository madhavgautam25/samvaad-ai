from app.tools.weather import WeatherTool


class ToolRouter:

    def __init__(self):

        self.tools = {

            "weather": WeatherTool()

        }

    def execute(self, action, message):

        tool = self.tools.get(action)

        if tool:

            return tool.execute(message)

        return None