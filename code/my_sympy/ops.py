import numpy


class Ops:
    # Класс - хранилище математических операций
    # Полностью состоит из статических методов
    @staticmethod
    def op_plus(stack):
        """
        Операция суммы
        :param stack: list
        :return: float
        """
        a = stack[0]
        b = stack[1]
        ans = a + b
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_minus(stack):
        """
        Операция разности
        :param stack: list
        :return: float
        """
        a = stack[0]
        b = stack[1]
        ans = b - a
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_mul(stack):
        """
        Операция умножения
        :param stack: list
        :return: float
        """
        a = stack[0]
        b = stack[1]
        ans = b * a
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_div(stack):
        """
        Операция деления
        :param stack: list
        :return: float
        """
        a = stack[0]
        b = stack[1]
        ans = b / a
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_deg(stack):
        """
        операция возведения в степень
        :param stack: list
        :return: float
        """
        a = stack[0]
        b = stack[1]
        ans = b ** a
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_opposite(stack):
        """
        операция смены знака на противоположный
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return -a

    @staticmethod
    def op_odiv(stack):
        """
        операция деления по модулю
        :param stack: list
        :return: float
        """
        a = stack[0]
        b = stack[1]
        ans = b % a
        stack.pop(0)
        stack.pop(0)
        return ans

    @staticmethod
    def op_sin(stack):
        """
        Операция синус
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return numpy.sin(a)

    @staticmethod
    def op_cos(stack):
        """
        Операция коминус
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return numpy.cos(a)

    @staticmethod
    def op_tan(stack):
        """
        Операция тангенс
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return numpy.tan(a)

    @staticmethod
    def op_asin(stack):
        """
        Операция арктангенс
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return numpy.arcsin(a)

    @staticmethod
    def op_acos(stack):
        """
        Операция арккосинус
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return numpy.arccos(a)

    @staticmethod
    def op_atan(stack):
        """
        Операция арктангенс
        :param stack: list
        :return: float
        """
        a = stack[0]
        stack.pop(0)
        return numpy.arctan(a)
