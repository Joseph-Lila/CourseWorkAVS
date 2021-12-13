from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivymd.uix.card import MDCard

x = [1, 2, 3, 4, 5]
y = [5, 12, 6, 9, 15]

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")


class Graph(MDCard):
    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)

        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

