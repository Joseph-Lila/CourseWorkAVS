from kivymd.app import MDApp
from Code.Logic.GUILogicBuilder import GUILogicBuilder


class GUILogic(MDApp):
    def __init__(self, **kwargs):
        self.title = "Решаю краевые задачи"
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        return GUILogicBuilder.form_main_cont()



