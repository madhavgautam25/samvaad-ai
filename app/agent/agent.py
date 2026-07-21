from app.agent.decision_engine import DecisionEngine
from app.tools.tool_router import ToolRouter


class Agent:

    def __init__(self, ai_engine):
        self.ai = ai_engine
        self.router = ToolRouter()
        self.decision = DecisionEngine()

    def run(self, messages):

        # Get the latest user message
        last_message = messages[-1]["content"]

        # Decide whether to use a tool
        decision = self.decision.decide(last_message)

        tool = decision.get("tool", "chat")

        # Execute the selected tool
        if tool != "chat":

            payload = decision.get("input", "")

            return self.router.execute(
                tool,
                payload
            )

        # Otherwise, use the LLM for normal conversation
        return self.ai.generate(messages)