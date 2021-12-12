import unittest
import numpy
from ..ExpressionSolver.Operations import Operations


class OperationsTestCase(unittest.TestCase):
    def test_op_plus(self):
        function = Operations.op_plus
        lst = [1, 1]
        self.assertEqual(2, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(-5, function([-1, -4]))
        self.assertEqual(1000, function([200, 800]))

    def test_op_minus(self):
        function = Operations.op_minus
        lst = [1, 1]
        self.assertEqual(0, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(-5, function([0, 5]))
        self.assertEqual(-600, function([200, 800]))

    def test_op_mul(self):
        function = Operations.op_mul
        lst = [1, 1]
        self.assertEqual(1, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(-5, function([-1, 5]))
        self.assertEqual(1000, function([20, 50]))

    def test_op_div(self):
        function = Operations.op_div
        lst = [1, 1]
        self.assertEqual(1, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(-0.2, function([-1, 5]))
        self.assertEqual(4, function([20, 5]))

    def test_op_deg(self):
        function = Operations.op_deg
        lst = [1, 1]
        self.assertEqual(1, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(8, function([2, 3]))
        self.assertEqual(100, function([10, 2]))

    def test_op_opposite(self):
        function = Operations.op_opposite
        lst = [1]
        self.assertEqual(-1, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(-5, function([5]))
        self.assertEqual(10.1, function([-10.1]))

    def test_op_odiv(self):
        function = Operations.op_odiv
        lst = [1, 4]
        self.assertEqual(1, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(10, function([10, 11]))
        self.assertEqual(3.3, function([3.3, 4]))

    def test_op_sin(self):
        function = Operations.op_sin
        lst = [0]
        self.assertEqual(0, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(numpy.sin(numpy.pi / 6), function([numpy.pi / 6]))

    def test_op_cos(self):
        function = Operations.op_cos
        lst = [0]
        self.assertEqual(1, function(lst))
        self.assertEqual([], lst)
        self.assertEqual(numpy.cos(numpy.pi / 6), function([numpy.pi / 6]))

    def test_op_tan(self):
        function = Operations.op_tan
        self.assertEqual(numpy.tan(numpy.pi / 6), function([numpy.pi / 6]))

    def test_op_asin(self):
        function = Operations.op_asin
        self.assertEqual(numpy.arcsin(numpy.pi / 6), function([numpy.pi / 6]))

    def test_op_acos(self):
        function = Operations.op_acos
        self.assertEqual(numpy.arccos(numpy.pi / 6), function([numpy.pi / 6]))

    def test_op_atan(self):
        function = Operations.op_atan
        self.assertEqual(numpy.arctan(numpy.pi / 6), function([numpy.pi / 6]))
