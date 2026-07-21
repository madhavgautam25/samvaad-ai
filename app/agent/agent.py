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

            return self.router.execute(
                tool,
                decision
            )

        return self.ai.generate(messages)