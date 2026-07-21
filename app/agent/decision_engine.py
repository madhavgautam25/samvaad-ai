import re


class DecisionEngine:

    def decide(self, message: str):

        msg = message.lower().strip()

        # ---------------- Weather ---------------- #

        weather_keywords = [
            "weather",
            "temperature",
            "forecast",
            "rain",
            "umbrella",
            "humidity",
            "wind"
        ]

        if any(word in msg for word in weather_keywords):
            return {
                "tool": "weather",
                "input": message
            }

        # ---------------- Calculator ---------------- #

        calculator_keywords = [
            "calculate",
            "calc",
            "plus",
            "minus",
            "multiply",
            "multiplied",
            "divide",
            "divided",
            "mod",
            "power",
            "sqrt",
            "log"
        ]

        math_symbols = re.search(r"[0-9+\-*/()%^.]", msg)

        if any(word in msg for word in calculator_keywords) or math_symbols:
            return {
                "tool": "calculator",
                "input": message
            }

        # ---------------- Default Chat ---------------- #

        return {
            "tool": "chat"
        }