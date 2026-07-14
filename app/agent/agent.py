from app.agent.decision_engine import DecisionEngine
from app.tools.tool_router import ToolRouter


class Agent:

    def __init__(self, ai_engine):

        self.ai = ai_engine

        self.router = ToolRouter()

        self.decision = DecisionEngine()

    def run(self, messages):

        last_message = messages[-1]["content"]

        action = self.decision.decide(last_message)

        if action != "chat":

            return self.router.execute(
                action,
                last_message
            )

        return self.ai.generate(messages)