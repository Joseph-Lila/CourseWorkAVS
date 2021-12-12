from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from functools import partial
from Graph.Graph import Graph


class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Решаю краевые задачи"
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        Builder.load_file('kv_files\\graph.kv')
        return Graph()


if __name__ == "__main__":
    Window.maximize()
    MyApp().run()
