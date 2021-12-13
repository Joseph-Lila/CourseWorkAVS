class Validator:
    def __init__(self, widgets):
        self.widgets = widgets

    def check_txt_fields_not_empty(self) -> bool:
        for key, value in self.widgets.items():
            if "txt" in key:
                if value.text == '':
                    return False
        return True
