import numpy as np
from Code.ExpressionSolver.ExpressionSolver import ExpressionSolver


class RungeKutForKoshi:
    @staticmethod
    def calculate(x0, xn, h, y0, z0, u, v):
        t = list(np.arange(x0, xn + h / 2, h))
        f = [y0]
        p = [z0]
        for i in range(1, len(t)):
            k1 = ExpressionSolver().calculate([v, "z=" + str(p[-1]), "y=" + str(f[-1]), "x=" + str(t[i - 1])], 3)
            q1 = ExpressionSolver().calculate([u, "z=" + str(p[-1]), "y=" + str(f[-1]), "x=" + str(t[i - 1])], 3)
            if k1 is None or q1 is None:
                return (None, ), (None, )
            k2 = ExpressionSolver().calculate\
                ([v, "z=" + str(p[-1] + q1 * h / 2), "y=" + str(f[-1] + k1 * h / 2), "x=" + str(t[i - 1] + h / 2)], 3)
            q2 = ExpressionSolver().calculate\
                ([u, "z=" + str(p[-1] + q1 * h / 2), "y=" + str(f[-1] + k1 * h / 2), "x=" + str(t[i - 1] + h / 2)], 3)
            if k2 is None or q2 is None:
                return (None, ), (None, )
            k3 = ExpressionSolver().calculate\
                ([v, "z=" + str(p[-1] + q2 * h / 2), "y=" + str(f[-1] + k2 * h / 2), "x=" + str(t[i - 1] + h / 2)], 3)
            q3 = ExpressionSolver().calculate\
                ([u, "z=" + str(p[-1] + q2 * h / 2), "y=" + str(f[-1] + k2 * h / 2), "x=" + str(t[i - 1] + h / 2)], 3)
            if k3 is None or q3 is None:
                return (None, ), (None, )
            k4 = ExpressionSolver().calculate\
                ([v, "z=" + str(p[-1] + q3 * h), "y=" + str(f[-1] + k3 * h), "x=" + str(t[i - 1] + h)], 3)
            q4 = ExpressionSolver().calculate\
                ([u, "z=" + str(p[-1] + q3 * h), "y=" + str(f[-1] + k3 * h), "x=" + str(t[i - 1] + h)], 3)
            if k4 is None or q4 is None:
                return (None, ), (None, )
            f.append(f[i - 1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
            p.append(p[i - 1] + h / 6 * (q1 + 2 * q2 + 2 * q3 + q4))
        return t.copy(), f.copy()
