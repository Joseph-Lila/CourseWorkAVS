from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from functools import partial
from Code.Graph.Graph import Graph
from Code.GUI.GUIBuilder import GUIBuilder


class GUILogic(MDApp):
    def __init__(self, **kwargs):
        self.title = "Решаю краевые задачи"
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        main_cont = GUIBuilder.my_grid_layout()
        main_cont.cols = 1
        main_cont.rows = None
        card = GUIBuilder.my_card()
        box1 = GUIBuilder.my_box_layout()
        box1.size_hint_y = .8
        box1.pos_hint = {"top": 1}
        box1.add_widget(Graph())
        my_button = GUIBuilder.my_button()
        card.add_widget(box1)
        card.add_widget(my_button)
        main_cont.add_widget(card)
        return main_cont
