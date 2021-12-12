import unittest
import unittest.mock
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard


class GUIBuilderTestCase(unittest.TestCase):
    def test_get_input(self):
        my_input = unittest.mock.MagicMock(spec=MDTextField)
        self.assertIsInstance(my_input, MDTextField)

    def test_get_label(self):
        my_label = unittest.mock.MagicMock(spec=MDLabel)
        self.assertIsInstance(my_label, MDLabel)

    def test_get_card(self):
        card = unittest.mock.MagicMock(spec=MDCard)
        self.assertIsInstance(card, MDCard)


if __name__ == '__main__':
    unittest.main()
