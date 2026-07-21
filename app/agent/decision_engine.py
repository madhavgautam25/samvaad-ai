class DecisionEngine:

    def decide(self, message: str):

        message = message.lower()

        # Weather Tool
        weather_keywords = [
            "weather",
            "temperature",
            "forecast",
            "rain",
            "humidity",
            "wind",
            "climate"
        ]

        if any(keyword in message for keyword in weather_keywords):
            return {
                "tool": "weather",
                "input": message
            }

        # Calculator Tool
        calculator_keywords = [
            "+", "-", "*", "/", "%",
            "calculate",
            "calc",
            "solve",
            "plus",
            "minus",
            "times",
            "multiplied",
            "multiply",
            "divided",
            "divide",
            "mod",
            "power",
            "raised"
        ]

        if any(keyword in message for keyword in calculator_keywords):
            return {
                "tool": "calculator",
                "input": message
            }

        # Date & Time Tool
        datetime_keywords = [
            "time",
            "date",
            "today",
            "day",
            "clock",
            "yesterday",
            "tomorrow",
            "current time",
            "current date"
        ]

        if any(keyword in message for keyword in datetime_keywords):
            return {
                "tool": "datetime",
                "input": message
            }

        # Default AI Chat
        return {
            "tool": "chat",
            "input": message
        }