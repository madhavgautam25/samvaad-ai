from datetime import datetime, timedelta


class DateTimeTool:

    def execute(self, query: str):

        query = query.lower()

        now = datetime.now()
        target_date = now

        # Relative dates
        if "day before yesterday" in query:
            target_date = now - timedelta(days=2)

        elif "yesterday" in query:
            target_date = now - timedelta(days=1)

        elif "day after tomorrow" in query:
            target_date = now + timedelta(days=2)

        elif "tomorrow" in query:
            target_date = now + timedelta(days=1)

        response = {
            "success": True,
            "tool": "datetime"
        }

        # Date
        if "date" in query:
            response["date"] = target_date.strftime("%d %B %Y")

        # Day
        if "day" in query:
            response["day"] = target_date.strftime("%A")

        # Time (always current)
        if "time" in query or "clock" in query:
            response["time"] = now.strftime("%I:%M:%S %p")

        # General query
        if len(response) == 2:
            response["date"] = target_date.strftime("%d %B %Y")
            response["day"] = target_date.strftime("%A")
            response["time"] = now.strftime("%I:%M:%S %p")

        return response