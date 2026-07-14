class DecisionEngine:

    def decide(self, message: str):

        text = message.lower()

        if any(word in text for word in [
            "weather",
            "temperature",
            "forecast",
            "rain"
        ]):
            return "weather"

        if any(word in text for word in [
            "calculate",
            "+",
            "-",
            "*",
            "/"
        ]):
            return "calculator"

        if any(word in text for word in [
            "time",
            "clock"
        ]):
            return "time"

        return "chat"