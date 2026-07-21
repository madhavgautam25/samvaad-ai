import re


class ExpressionParser:

    def parse(self, message: str) -> str:

        expression = message.lower().strip()

        # Remove common words
        words = [
            "what is",
            "calculate",
            "calc",
            "solve",
            "equals",
            "=",
            "please",
            "can you",
            "find"
        ]

        for word in words:
            expression = expression.replace(word, "")

        # Convert words to operators
        replacements = {
            "plus": "+",
            "minus": "-",
            "times": "*",
            "multiplied by": "*",
            "multiply by": "*",
            "x": "*",
            "into": "*",
            "divided by": "/",
            "divide by": "/",
            "mod": "%",
            "modulus": "%",
            "power of": "**",
            "raised to": "**"
        }

        for key, value in replacements.items():
            expression = expression.replace(key, value)

        # Remove spaces
        expression = expression.replace(" ", "")

        # Keep only valid calculator characters
        expression = re.sub(r"[^0-9+\-*/().%*]", "", expression)

        return expression