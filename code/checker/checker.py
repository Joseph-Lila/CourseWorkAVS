class Checker:
    def __init__(self, widgets):
        """
        Класс для валидации полей ввода GUI
        :param widgets:
        """
        self.widgets = widgets

    def check_txt_fields_not_empty(self) -> bool:
        """
        Функция проверяющая заполненность каждого поля ввода.
        :return: bool
        """
        for key, value in self.widgets.items():
            if "txt" in key:
                if value.get() == '':
                    return False
        return True
