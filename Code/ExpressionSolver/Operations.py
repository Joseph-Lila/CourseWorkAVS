import numpy


class Operations:
    @staticmethod
    def op_plus(stack):
        a = stack[0]
        b = stack[1]
        ans = a + b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_minus(stack):
        a = stack[0]
        b = stack[1]
        ans = a - b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_mul(stack):
        a = stack[0]
        b = stack[1]
        ans = a * b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_div(stack):
        a = stack[0]
        b = stack[1]
        ans = a / b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_deg(stack):
        a = stack[0]
        b = stack[1]
        ans = a ** b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_opposite(stack):
        a = stack[0]
        stack.pop(0)
        return -a

    @staticmethod
    def op_odiv(stack):
        a = stack[0]
        b = stack[1]
        ans = a % b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_sin(stack):
        a = stack[0]
        stack.pop(0)
        return numpy.sin(a)

    @staticmethod
    def op_cos(stack):
        a = stack[0]
        stack.pop(0)
        return numpy.cos(a)

    @staticmethod
    def op_tan(stack):
        a = stack[0]
        stack.pop(0)
        return numpy.tan(a)

    @staticmethod
    def op_asin(stack):
        a = stack[0]
        stack.pop(0)
        return numpy.arcsin(a)

    @staticmethod
    def op_acos(stack):
        a = stack[0]
        stack.pop(0)
        return numpy.arccos(a)

    @staticmethod
    def op_atan(stack):
        a = stack[0]
        stack.pop(0)
        return numpy.arctan(a)
