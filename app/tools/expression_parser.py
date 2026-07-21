import re


class ExpressionParser:

    def __init__(self):

        self.replacements = {
            "multiplied by": "*",
            "multiply by": "*",
            "times": "*",
            "into": "*",
            "x": "*",

            "divided by": "/",
            "divide by": "/",
            "over": "/",

            "plus": "+",
            "add": "+",

            "minus": "-",
            "subtract": "-",

            "modulus": "%",
            "mod": "%",

            "raised to": "**",
            "power of": "**",
            "to the power of": "**"
        }

        self.remove_words = [
            "what is",
            "calculate",
            "compute",
            "solve",
            "find",
            "evaluate",
            "please",
            "can you",
            "could you",
            "tell me",
            "answer",
            "equals",
            "=",
            "?",
            ","
        ]

    def parse(self, message: str) -> str:

        expression = message.lower().strip()

        # Remove unnecessary words
        for word in self.remove_words:
            expression = expression.replace(word, " ")

        # Replace English operators
        for word, symbol in self.replacements.items():
            expression = expression.replace(word, f" {symbol} ")

        # Normalize spaces
        expression = re.sub(r"\s+", " ", expression).strip()

        # Remove spaces around operators
        expression = expression.replace(" ", "")

        # Keep only valid mathematical characters
        expression = re.sub(r"[^0-9+\-*/().%]", "", expression)

        return expression