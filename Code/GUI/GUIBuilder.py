from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard


class GUIBuilder:
    @staticmethod
    def get_input():
        my_input = MDTextField(
            pos_hint={"center_x": .5},
            icon_right_color=[1, 0, 1, 1],
            helper_text='Check the field!',
            helper_text_mode='on_error',
            color_mode='primary',
            mode='rectangle',
            size_hint_y=None,
            size_hint_x=None,
            height=40,
            font_size=20,
            width=220,
            write_tab=False,
        )
        return my_input

    @staticmethod
    def get_label():
        label = MDLabel(
            font_style='Button',
            halign='center',
            size_hint_y=None,
            text="Hi",
            color=[40 / 255, 40 / 255, 180 / 255, 150 / 255]
        )
        return label

    @staticmethod
    def get_card():
        card = MDCard(
            size_hint=(.7, .8),
            pos_hint={"center_x": .5, "center_y": .5},
            elevation=15,
            padding=20,
            spacing=20,
            orientation='vertical',
            md_bg_color=[10 / 255, 10 / 255, 140 / 255, 100 / 255]
        )
        return card
