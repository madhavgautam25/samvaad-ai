import re


class ProfileManager:

    @staticmethod
    def extract_name(message):

        patterns = [

            r"my name is (.+)",

            r"i am (.+)",

            r"i'm (.+)"

        ]

        text = message.lower()

        for pattern in patterns:

            match = re.search(pattern, text)

            if match:

                return match.group(1).strip().title()

        return None