from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivymd.uix.card import MDCard
from Code.PointsKeeper.PointsKeeper import points_set


class Graph(MDCard):

    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)
        self.update_plt()

    def update_plt(self, *args):
        self.clear_widgets()
        x = points_set()[0]
        y = points_set()[1]
        current_figure = plt.figure()
        plt.plot(x, y)
        plt.ylabel("Ось Y")
        plt.xlabel("Ось X")
        plt.figure(current_figure.number)
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

