from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 12, 6, 9, 15]

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")


class Graph(FloatLayout):
    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)

        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

