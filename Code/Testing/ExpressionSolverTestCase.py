import unittest
from Code.ExpressionSolver.ExpressionSolver import ExpressionSolver


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
        function = ExpressionSolver().create_tokens_from_expression
        self.assertEqual(1, function("sin(x)"))
        