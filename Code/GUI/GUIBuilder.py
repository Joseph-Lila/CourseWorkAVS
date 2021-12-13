from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivy.uix.image import Image
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.widget import Widget


class GUIBuilder:
    @staticmethod
    def my_text_field():
        my_input = MDTextField()
        my_input.pos_hint = {"center_x": .5}
        my_input.icon_right_color = (1, 1, 1, 1)
        my_input.size_hint = (None, None)
        my_input.font_size = 25
        my_input.mode = 'rectangle'
        my_input.color_mode = 'accent'
        my_input.width = 200
        my_input.write_tab = False
        my_input.text_color = (255 / 255, 215 / 255, 0 / 255, 1)
        my_input.md_bg_color = (255 / 255, 215 / 255, 0 / 255, 1)
        return my_input

    @staticmethod
    def my_widget():
        widget = Widget()
        widget.pos_hint = {"center_x": .5}
        widget.size_hint = (None, None)
        return widget

    @staticmethod
    def my_label():
        label = MDLabel()
        label.pos_hint = {"center_x": .5}
        label.halign = "center"
        label.size_hint = (None, None)
        label.text = "Hi"
        label.font_size = 25
        label.width = 100
        label.height = 68
        label.color = (40 / 255, 40 / 255, 180 / 255, 255 / 255)
        label.md_bg_color = (40 / 255, 40 / 255, 180 / 255, 150 / 255)
        return label

    @staticmethod
    def my_card():
        card = MDCard()
        card.size_hint = (.7, .8)
        card.pos_hint = {"center_x": .5, "center_y": .5}
        card.elevation = 15
        card.padding = 20
        card.spacing = 20
        card.orientation = 'vertical'
        card.md_bg_color = [255/255, 151/255, 187/255, 1]
        return card

    @staticmethod
    def my_button():
        button = MDFillRoundFlatButton(
            pos_hint={"center_x": .5},
            font_size=20,
            md_bg_color=[10 / 255, 10 / 255, 140 / 255, 100 / 255],
            text_color=[0, 0, 0, 1],
            size_hint_x=None
        )
        return button

    @staticmethod
    def my_icon_button():
        button = MDFillRoundFlatIconButton(
            pos_hint={"center_x": .5},
            font_size=15,
            md_bg_color=[40 / 255, 40 / 255, 180 / 255, 100 / 255],
            text_color=[1, 1, 1, 1],
            size_hint_x=None
        )
        return button

    @staticmethod
    def my_image():
        image = Image(
            pos_hint={"center_x": .5, "center_y": .5},
            allow_stretch=True,
            size_hint=(1, 1)
        )
        return image

    @staticmethod
    def my_grid_layout():
        grid = GridLayout()
        grid.spacing = 15
        grid.pos_hint = {"center_x": .5, "center_y": .5}
        grid.minimum_height = 1
        return grid

    @staticmethod
    def my_box_layout():
        return BoxLayout()

    @staticmethod
    def my_file_manager():
        elem = MDFileManager()
        return elem
