from app.tools.weather import WeatherTool
from app.tools.calculator import CalculatorTool
from app.tools.datetime_tool import DateTimeTool


class ToolRouter:

    def __init__(self):

        self.tools = {
            "weather": WeatherTool(),
            "calculator": CalculatorTool(),
            "datetime": DateTimeTool()
        }

    def execute(self, tool_name, payload):

        tool = self.tools.get(tool_name)

        if not tool:
            return {
                "success": False,
                "message": f"Unknown tool: {tool_name}"
            }

        return tool.execute(payload)