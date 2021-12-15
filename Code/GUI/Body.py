import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
from Code.PointsKeeper.PointsKeeper import points_set
from Code.Validation.Validator import Validator
from Code.BoundaryValueProblem.FiringMethod import FiringMethod
from Code.PointsKeeper.PointsKeeper import change_set


class Body:
    def __init__(self):
        self.master = tk.Tk()
        self.elements = dict()
        self.master.geometry('1000x800')
        self.form_elements()

    def form_elements(self):
        standard_step = 25
        matplotlib.use('TkAgg')
        self.elements["fig"] = plt.figure(1)
        self.elements["canvas"] = FigureCanvasTkAgg(self.elements["fig"], master=self.master)
        self.elements["plot_widget"] = self.elements["canvas"].get_tk_widget()
        self.elements["plot_widget"].place(x=standard_step * 6, y=standard_step * 6)

        self.elements["main_label"] = tk.Label(self.master, text="f'' = c0 * 1 + c1 * x + c2 * y + c3 * y'").\
            place(x=standard_step * 15, y=standard_step * 0)

        self.elements["label_c0"] = tk.Label(self.master, text='c0').place(x=standard_step * 9, y=standard_step * 1)
        self.elements["label_c1"] = tk.Label(self.master, text='c1').place(x=standard_step * 9, y=standard_step * 2)
        self.elements["label_c2"] = tk.Label(self.master, text='c2').place(x=standard_step * 9, y=standard_step * 3)
        self.elements["label_c3"] = tk.Label(self.master, text='c3').place(x=standard_step * 9, y=standard_step * 4)

        self.elements["txt_field_c0"] = tk.Entry(self.master, width=standard_step * 1).\
            place(x=standard_step * 10, y=standard_step * 1)
        self.elements["txt_field_c1"] = tk.Entry(self.master, width=standard_step * 1).\
            place(x=standard_step * 10, y=standard_step * 2)
        self.elements["txt_field_c2"] = tk.Entry(self.master, width=standard_step * 1).\
            place(x=standard_step * 10, y=standard_step * 3)
        self.elements["txt_field_c3"] = tk.Entry(self.master, width=standard_step * 1).\
            place(x=standard_step * 10, y=standard_step * 4)

        self.elements['q1'] = tk.Label(self.master, text='y(').place(x=standard_step * 20, y=standard_step * 2)
        self.elements['q2'] = tk.Label(self.master, text=') = ').place(x=standard_step * 23, y=standard_step * 2)
        self.elements['q3'] = tk.Label(self.master, text='y(').place(x=standard_step * 20, y=standard_step * 3)
        self.elements['q4'] = tk.Label(self.master, text=') = ').place(x=standard_step * 23, y=standard_step * 3)

        self.elements["txt_field_a"] = tk.Entry(self.master, width=int(standard_step * 1 / 4)).\
            place(x=standard_step * 21, y=standard_step * 2)
        self.elements["txt_field_b"] = tk.Entry(self.master, width=int(standard_step * 1 / 4)).\
            place(x=standard_step * 21, y=standard_step * 3)
        self.elements["txt_field_y_a"] = tk.Entry(self.master, width=int(standard_step * 1 / 4)).\
            place(x=standard_step * 24, y=standard_step * 2)
        self.elements["txt_field_y_b"] = tk.Entry(self.master, width=int(standard_step * 1 / 4)).\
            place(x=standard_step * 24, y=standard_step * 3)

        self.elements["btn"] = tk.Button(self.master, text="Построить график.", command=self.update_plt).\
            place(x=standard_step * 17, y=standard_step * 27)

    def get_master(self):
        return self.master

    def update_plt(self, *args):
        if not Validator(self.elements).check_txt_fields_not_empty():
            return None
        try:
            kwargs = {
                        "u": "(" + self.elements["txt_field_c0"].text + ") * 1 + (" +
                             self.elements["txt_field_c1"].text + ") * x + (" +
                             self.elements["txt_field_c2"].text + ") * y + (" +
                             self.elements["txt_field_c3"].text + ") * z",
                        "v": "z",
                        "a": float(self.elements["txt_field_a"].text),
                        "b": float(self.elements["txt_field_b"].text),
                        "ya": float(self.elements["txt_field_y_a"].text),
                        "yb": float(self.elements["txt_field_y_b"].text)
                    }
        except:
            return None
        points = FiringMethod(
            kwargs["u"],
            kwargs["v"],
            kwargs["a"],
            kwargs["b"],
            kwargs["ya"],
            kwargs["yb"]
        ).get_points()
        if points is not None:
            change_set(*points)
        plt.clf()
        sets_ = points_set()
        plt.plot(*sets_)
        self.elements["fig"].canvas.draw()
