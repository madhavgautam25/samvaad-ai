import ast
import operator
from app.tools.expression_parser import ExpressionParser

class CalculatorTool:

    def __init__(self):

        self.parser = ExpressionParser()
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos
        }

    def execute(self, expression):

        try:

            expression = self.parser.parse(expression)

            result = self.evaluate(expression)

            return {
                "success": True,
                "tool": "calculator",
                "result": result
            }

        except ZeroDivisionError:

            return {
                "success": False,
                "message": "Division by zero is not allowed."
            }

        except Exception:

            return {
                "success": False,
                "message": "Invalid mathematical expression."
            }

    def evaluate(self, expression):

        tree = ast.parse(expression, mode="eval")

        return self.visit(tree.body)

    def visit(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.Num):
            return node.n

        elif isinstance(node, ast.BinOp):

            left = self.visit(node.left)
            right = self.visit(node.right)

            operator_func = self.operators[type(node.op)]

            return operator_func(left, right)

        elif isinstance(node, ast.UnaryOp):

            value = self.visit(node.operand)

            operator_func = self.operators[type(node.op)]

            return operator_func(value)

        raise ValueError("Unsupported expression")