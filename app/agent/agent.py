from app.agent.decision_engine import DecisionEngine
from app.tools.tool_router import ToolRouter


class Agent:

    def __init__(self, ai_engine):
        self.ai = ai_engine
        self.router = ToolRouter()
        self.decision = DecisionEngine()

    def run(self, messages):

        last_message = messages[-1]["content"]

        decision = self.decision.decide(last_message)

        tool = decision.get("tool", "chat")

        if tool != "chat":

            payload = decision.get("input", "")

            tool_response = self.router.execute(
                tool,
                payload
            )

            if tool == "search" and tool_response.get("success"):

                prompt = f"""
    You are Samvaad AI.

    Answer the user's question using ONLY the search results below.

    Question:
    {payload}

    Search Results:
    {tool_response['context']}

    Instructions:

    - Give a natural answer.
    - Do not mention JSON.
    - Keep it concise.
    - Mention the sources at the end.
    """

                return self.ai.generate([
                    {
                        "role": "user",
                        "content": prompt
                    }
                ])

            return tool_response

        return self.ai.generate(messages)