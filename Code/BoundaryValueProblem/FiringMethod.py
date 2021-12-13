import numpy as np
from Code.BoundaryValueProblem.RungeKutForKoshi import RungeKutForKoshi
from Code.GUI.Notification import Notification


class FiringMethod:
    h = 0.05
    e = 0.001
    dialog = None
    note = Notification(dialog)

    def __init__(self, u, v, a, b, ya, yb):
        self.u = u
        self.v = v
        self.a = a
        self.b = b
        self.ya = ya
        self.yb = yb

    def __find_angles(self):
        strong_angle = np.pi / 2 - 1e-3
        weak_angle = - np.pi / 2 + 1e-3
        strong_res = RungeKutForKoshi.calculate(
            self.a,
            self.b,
            self.h,
            self.ya,
            np.tan(strong_angle),
            self.u,
            self.v
        )[1][-1]
        weak_res = RungeKutForKoshi.calculate(
            self.a,
            self.b,
            self.h,
            self.ya,
            np.tan(weak_angle),
            self.u,
            self.v
        )[1][-1]
        if strong_res is None or weak_res is None:
            return None, None
        if strong_res > self.yb > weak_res:
            return strong_angle, weak_angle
        return None, None

    def __processing(self):
        strong_angle, weak_angle = self.__find_angles()
        if strong_angle is None or weak_angle is None:
            return None
        while abs(RungeKutForKoshi.calculate(self.a, self.b, self.h, self.ya, np.tan(weak_angle),
                                             self.u, self.v)[1][-1] - self.yb) > self.e:
            res = RungeKutForKoshi.calculate(self.a, self.b, self.h, self.ya, np.tan((weak_angle + strong_angle) / 2),
                                             self.u, self.v)[1][-1]
            if res <= self.yb:
                weak_angle = (weak_angle + strong_angle) / 2
            else:
                strong_angle = (weak_angle + strong_angle) / 2
        return weak_angle

    def get_points(self):
        angle = self.__processing()
        if angle is None:
            self.note.universal_note("Задача неразрешима!", [])
            return None
        return RungeKutForKoshi.calculate(self.a, self.b, self.h, self.ya, np.tan(angle), self.u, self.v)
