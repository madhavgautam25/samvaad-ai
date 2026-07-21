from app.tools.weather import WeatherTool
from app.tools.calculator import CalculatorTool
from app.tools.datetime_tool import DateTimeTool
from app.tools.search_tool import SearchTool


class ToolRouter:

    def __init__(self):

        self.tools = {
            "weather": WeatherTool(),
            "calculator": CalculatorTool(),
            "datetime": DateTimeTool(),
            "search": SearchTool()
        }

    def execute(self, tool_name, query):

        tool = self.tools.get(tool_name)

        if tool is None:
            return {
                "success": False,
                "message": "Tool not found."
            }

        return tool.execute(query)