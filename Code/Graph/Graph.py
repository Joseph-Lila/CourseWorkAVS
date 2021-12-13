from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivymd.uix.card import MDCard
from Code.PointsKeeper.PointsKeeper import points_set


class Graph(MDCard):
    limit = 10

    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)
        self.update_plt()

    def update_plt(self, *args):
        self.clear_widgets()
        sets_ = points_set()
        plt.close(plt.figure())
        current_figure = plt.figure()
        if len(sets_) > Graph.limit:
            for i in range(Graph.limit):
                plt.plot(*sets_[i])
        else:
            for item in sets_:
                plt.plot(*item)
        plt.ylabel("Ось Y")
        plt.xlabel("Ось X")
        plt.figure(current_figure.number)
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

