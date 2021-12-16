# импорт библиотек
# numpy - пакет для оптимизированных вычислений
# Runge - пользовательский класс для решения ДУ методо Рунге-Кутта 4-го порядка
# Точность численного метода: O(h^5) для каждого шага и O(h^4) - суммарная точность, где h - шаг
import numpy as np
from code.boundary_problem.runge import Runge


class FiringMethod:
    h = 0.05
    e = 0.001
    dialog = None

    def __init__(self, u, v, a, b, ya, yb):
        """
        Инициализация необходимых параметров для Метода Стрельбы.
        :param u: строка, содержащая правую часть выражения y'' = c0 * 1 + c1 * x + x2 * y + c3 * y'
        :param v: всегда является строкой 'y'=z'
        :param a: начало интервала переменной x
        :param b: конец интервала переменной x
        :param ya: значение y(a)
        :param yb: значение y(b)
        """
        self.u = u
        self.v = v
        self.a = a
        self.b = b
        self.ya = ya
        self.yb = yb

    def __find_angle(self):
        """
        Функция поиска углов 'пристрелки'.
        Так как мы имеем дело с тангенсом, область определения от -Пи/2 до +Пи/2.
        В крайних точках тангенс равняется бесконечности, поэтому делается отступ на 1е-3.
        Таким образом охватывается почти все множество решений краевой задачи.
        :return: (double, double) ИЛИ (None, None).
        """
        strong_angle = np.pi / 2 - 1e-3
        weak_angle = - np.pi / 2 + 1e-3
        strong_res = Runge.solve(self.a, self.b, self.h, self.ya,
                                 np.tan(strong_angle), self.u, self.v)[1][-1]
        weak_res = Runge.solve(self.a, self.b, self.h, self.ya, np.tan(weak_angle),
                               self.u, self.v)[1][-1]
        if strong_res is None or weak_res is None:
            return None, None
        if strong_res > self.yb > weak_res:
            return strong_angle, weak_angle
        return None, None

    def __processing(self):
        """
        Бинарный поиск подходящего угла.
        :return: double
        """
        strong_angle, weak_angle = self.__find_angle()
        if strong_angle is None or weak_angle is None:
            return None
        while abs(Runge.solve(self.a, self.b, self.h, self.ya, np.tan(weak_angle),
                              self.u, self.v)[1][-1] - self.yb) > self.e:
            res = Runge.solve(self.a, self.b, self.h, self.ya, np.tan((weak_angle + strong_angle) / 2),
                              self.u, self.v)[1][-1]
            if res is None:
                return None
            if res <= self.yb:
                weak_angle = (weak_angle + strong_angle) / 2
            else:
                strong_angle = (weak_angle + strong_angle) / 2
        return weak_angle

    def get_solution(self):
        """
        Метод находит угол - искомый параметр при решении краевой задачи методом стрельбы.
        :return: (x, y), где x, y - списки со значениями типа double
        """
        angle = self.__processing()
        if angle is None:
            return None
        return Runge.solve(self.a, self.b, self.h, self.ya, np.tan(angle), self.u, self.v)
