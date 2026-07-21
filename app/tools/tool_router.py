from app.tools.weather import WeatherTool
from app.tools.calculator import CalculatorTool


class ToolRouter:

    def __init__(self):

        self.tools = {
            "weather": WeatherTool(),
            "calculator": CalculatorTool(),
        }

    def execute(self, tool_name, payload):

        tool = self.tools.get(tool_name)

        if not tool:
            return {
                "success": False,
                "message": f"Tool '{tool_name}' not found."
            }

        return tool.execute(payload)