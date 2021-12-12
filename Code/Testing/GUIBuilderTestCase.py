import unittest
import unittest.mock
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.filemanager import MDFileManager


class GUIBuilderTestCase(unittest.TestCase):
    def test_my_text_field(self):
        elem = unittest.mock.MagicMock(spec=MDTextField)
        self.assertIsInstance(elem, MDTextField)

    def test_my_label(self):
        elem = unittest.mock.MagicMock(spec=MDLabel)
        self.assertIsInstance(elem, MDLabel)

    def test_my_card(self):
        elem = unittest.mock.MagicMock(spec=MDCard)
        self.assertIsInstance(elem, MDCard)

    def test_my_button(self):
        elem = unittest.mock.MagicMock(spec=MDFillRoundFlatButton)
        self.assertIsInstance(elem, MDFillRoundFlatButton)

    def test_my_icon_button(self):
        elem = unittest.mock.MagicMock(spec=MDFillRoundFlatIconButton)
        self.assertIsInstance(elem, MDFillRoundFlatIconButton)

    def test_my_image(self):
        elem = unittest.mock.MagicMock(spec=Image)
        self.assertIsInstance(elem, Image)

    def test_my_grid_layout(self):
        elem = unittest.mock.MagicMock(spec=GridLayout)
        self.assertIsInstance(elem, GridLayout)

    def test_my_file_manager(self):
        elem = unittest.mock.MagicMock(spec=MDFileManager)
        self.assertIsInstance(elem, MDFileManager)


if __name__ == '__main__':
    unittest.main()
