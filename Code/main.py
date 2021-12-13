from kivy.core.window import Window
from Code.Logic.GUILogic import GUILogic


def main():
    Window.maximize()
    GUILogic().run()


if __name__ == "__main__":
    main()

