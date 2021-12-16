# tkinter - стандартная библиотека для создания графического интерфейса пользователя
import tkinter as tk
# FigureCanvasTkAgg - класс для создания холста-элемента GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
from tkinter import *
# импорт пользовательских библиотек
from code.points_store.points_store import points_store
from code.checker.checker import Checker
from code.boundary_problem.firing_method import FiringMethod
from code.points_store.points_store import change_store


class Body:
    def __init__(self):
        """
        Создание и инициалзация окна приложения
        """
        self.master = tk.Tk()
        self.elements = dict()
        self.master.geometry('1000x800')
        self.form_elements()

    def form_elements(self):
        """
        Создает все используемые элементы в приложении.
        Связывает кнопку с функцией обработки и отображения результатов решения краевой задачи.
        :return: None
        """
        # параметр для более удобного задания положения и размеров виджетов
        standard_step = 25
        # создание и подготовка к использованию холста-виджета
        matplotlib.use('TkAgg')
        self.elements["fig"] = plt.figure(1)
        self.elements["canvas"] = FigureCanvasTkAgg(self.elements["fig"], master=self.master)
        self.elements["plot_widget"] = self.elements["canvas"].get_tk_widget()
        self.elements["plot_widget"].place(x=standard_step * 6, y=standard_step * 6)

        # создание надписи структуры главного выражения для решения краевой задачи
        tk.Label(self.master, text="f'' = c0 * 1 + c1 * x + c2 * y + c3 * y'").\
            place(x=standard_step * 15, y=standard_step * 0)

        # создание полей ввода для коэффициентов главного выражения
        tk.Label(self.master, text='c0').place(x=standard_step * 9, y=standard_step * 1)
        tk.Label(self.master, text='c1').place(x=standard_step * 9, y=standard_step * 2)
        tk.Label(self.master, text='c2').place(x=standard_step * 9, y=standard_step * 3)
        tk.Label(self.master, text='c3').place(x=standard_step * 9, y=standard_step * 4)

        # подготовка переменных, хранящих содержимое полей ввода
        self.elements["txt_field_c0"] = StringVar()
        self.elements["txt_field_c1"] = StringVar()
        self.elements["txt_field_c2"] = StringVar()
        self.elements["txt_field_c3"] = StringVar()

        # создание полей ввода
        tk.Entry(self.master, width=standard_step * 1, textvariable=self.elements["txt_field_c0"])\
            .place(x=standard_step * 10, y=standard_step * 1)
        tk.Entry(self.master, width=standard_step * 1, textvariable=self.elements["txt_field_c1"])\
            .place(x=standard_step * 10, y=standard_step * 2)
        tk.Entry(self.master, width=standard_step * 1, textvariable=self.elements["txt_field_c2"])\
            .place(x=standard_step * 10, y=standard_step * 3)
        tk.Entry(self.master, width=standard_step * 1, textvariable=self.elements["txt_field_c3"])\
            .place(x=standard_step * 10, y=standard_step * 4)

        # создание надписей для ввода краевых условий краевой задачи
        tk.Label(self.master, text='y(').place(x=standard_step * 20, y=standard_step * 2)
        tk.Label(self.master, text=') = ').place(x=standard_step * 23, y=standard_step * 2)
        tk.Label(self.master, text='y(').place(x=standard_step * 20, y=standard_step * 3)
        tk.Label(self.master, text=') = ').place(x=standard_step * 23, y=standard_step * 3)

        # подготовка элементов, хранящих содержимое полей ввода
        self.elements["txt_field_a"] = StringVar()
        self.elements["txt_field_b"] = StringVar()
        self.elements["txt_field_y_a"] = StringVar()
        self.elements["txt_field_y_b"] = StringVar()

        # создание полей ввода
        tk.Entry(self.master, width=int(standard_step * 1 / 4), textvariable=self.elements["txt_field_a"])\
            .place(x=standard_step * 21, y=standard_step * 2)
        tk.Entry(self.master, width=int(standard_step * 1 / 4), textvariable=self.elements["txt_field_b"])\
            .place(x=standard_step * 21, y=standard_step * 3)
        tk.Entry(self.master, width=int(standard_step * 1 / 4), textvariable=self.elements["txt_field_y_a"])\
            .place(x=standard_step * 24, y=standard_step * 2)
        tk.Entry(self.master, width=int(standard_step * 1 / 4), textvariable=self.elements["txt_field_y_b"])\
            .place(x=standard_step * 24, y=standard_step * 3)

        # создание кнопки
        tk.Button(self.master, text="Построить график.", command=self.update_plt).\
            place(x=standard_step * 17, y=standard_step * 27)

    def get_master(self):
        """
        Геттер. Возвращает сущность окна приложения.
        :return: Tk (tkinter)
        """
        return self.master

    def update_plt(self, *args):
        """
        Функция обнвления холста.
        :param args: list
        :return: None
        """
        # проверка на пустоту элементов ввода.
        if not Checker(self.elements).check_txt_fields_not_empty():
            return None
        try:
            kwargs = {
                        "u": "(" + self.elements["txt_field_c0"].get() + ") * 1 + (" +
                             self.elements["txt_field_c1"].get() + ") * x + (" +
                             self.elements["txt_field_c2"].get() + ") * y + (" +
                             self.elements["txt_field_c3"].get() + ") * z",
                        "v": "z",
                        "a": float(self.elements["txt_field_a"].get()),
                        "b": float(self.elements["txt_field_b"].get()),
                        "ya": float(self.elements["txt_field_y_a"].get()),
                        "yb": float(self.elements["txt_field_y_b"].get())
                    }
        except:
            return None
        points = FiringMethod(kwargs["u"], kwargs["v"], kwargs["a"], kwargs["b"], kwargs["ya"], kwargs["yb"]).\
            get_solution()
        if points is not None:
            change_store(*points)
        plt.clf()
        sets_ = points_store()
        plt.plot(*sets_)
        self.elements["fig"].canvas.draw()
