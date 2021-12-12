import unittest
import numpy
from Code.ExpressionSolver.ExpressionSolver import ExpressionSolver, TokenType


class ExpressionSolverTestCase(unittest.TestCase):
    def test_read_expression_from_str(self):
        ans = ExpressionSolver().read_expression_from_str(["sin(x)", "x=0"], 1)
        self.assertEqual("sin(x)", ans)

    def test_is_delimiter(self):
        function = ExpressionSolver().is_delimiter
        self.assertTrue(function(" "))
        self.assertTrue(function("("))
        self.assertTrue(function(")"))
        self.assertTrue(function("+"))
        self.assertTrue(function("/"))
        self.assertTrue(function("*"))
        self.assertTrue(function("-"))
        self.assertTrue(function("^"))
        self.assertTrue(function("%"))

    def test_create_tokens_from_expression(self):
        solver = ExpressionSolver()
        expression = solver.read_expression_from_str(["sin(x)", "x=1.57"], 1)
        if expression is not None:
            solver.create_tokens_from_expression("sin(x)")
            self.assertEqual(len(solver.tokens), 4)
            self.assertEqual(solver.tokens[0].type, TokenType.func)
            self.assertEqual(solver.tokens[1].type, TokenType.op_br)
            self.assertEqual(solver.tokens[2].type, TokenType.var)
            self.assertEqual(solver.tokens[3].type, TokenType.cl_br)
        self.assertEqual(solver.variables["x"], 1.57)
        self.assertEqual(len(solver.variables), 1)

    def test_create_prior(self):
        solver = ExpressionSolver()
        self.assertEqual(len(solver.prior), 7)

    def test_create_postfix_from_tokens(self):
        solver = ExpressionSolver()
        expression = solver.read_expression_from_str(["sin(x)+y", "x=1.57", "y=2"], 2)
        if expression is not None:
            solver.create_tokens_from_expression("sin(x)+y")
            solver.create_postfix_from_tokens()
            self.assertEqual(len(solver.postfix_tokens), 4)
            self.assertEqual(solver.postfix_tokens[0].name, "x")
            self.assertEqual(solver.postfix_tokens[1].name, "sin")
            self.assertEqual(solver.postfix_tokens[2].name, "y")

    def test_create_ops(self):
        solver = ExpressionSolver()
        self.assertEqual(len(solver.ops), 13)

    def test_result_expression(self):
        solver = ExpressionSolver()
        expression = solver.read_expression_from_str(["sin(x)+y", "x=1.57", "y=2"], 2)
        if expression is not None:
            solver.create_tokens_from_expression(expression)
            solver.create_postfix_from_tokens()
            self.assertEqual(solver.result_expression(), numpy.sin(1.57) + 2)

    def test_calculate(self):
        input_str = ["tan(x)+y^2+z/10", "x=0", "y=2", "z=2"]
        quantity_variables = 3
        self.assertEqual(ExpressionSolver().calculate(input_str, quantity_variables), 4.2)
        self.assertEqual(None, ExpressionSolver().calculate(input_str, quantity_variables - 1))
        input_str = ["tan(x)+arcy^2+z/10", "x=0", "y=2", "z=2"]
        quantity_variables = 3
        self.assertEqual(ExpressionSolver().calculate(input_str, quantity_variables), None)
        input_str = ["tan(x)+y^2+z/10", "x=0", "x=2", "z=2"]
        quantity_variables = 3
        self.assertEqual(ExpressionSolver().calculate(input_str, quantity_variables), None)
        input_str = ["tan(x)+y^2+z/10", "x=0", "y=2", "f=2"]
        quantity_variables = 3
        self.assertEqual(ExpressionSolver().calculate(input_str, quantity_variables), None)
        input_str = ["-(10+x)+y", "x=5", "y=-10"]
        quantity_variables = 2
        self.assertEqual(ExpressionSolver().calculate(input_str, quantity_variables), -25)

