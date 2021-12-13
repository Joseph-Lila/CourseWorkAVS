from functools import partial
from Code.BoundaryValueProblem.FiringMethod import FiringMethod
from Code.PointsKeeper.PointsKeeper import clear_points_sets, add_points_set


class GUILogicBinder:
    def __init__(self, widgets):
        self.widgets = widgets
        self.functions = dict()
        self.params = dict()
        self.__form_functions()

    def __form_functions(self):
        self.functions["btn_update"] = self.widgets["graph"].update_plt
        self.params["btn_update"] = []
        self.functions["btn_clear"] = clear_points_sets
        self.params["btn_clear"] = []
        self.functions["btn_calculate"] = self.send_points_after_calculation
        self.params["btn_calculate"] = []
        self.functions["btn_import"] = print
        self.params["btn_import"] = []
        self.functions["btn_export"] = print
        self.params["btn_export"] = []

    def bind_widgets(self):
        # print("widgets: ", self.widgets.keys())
        # print("functions: ", self.functions.keys())
        # print("params: ", self.params.keys())
        for key, _ in self.functions.items():
            self.widgets[key].bind(on_press=partial(self.functions[key], self.params[key]))

    def send_points_after_calculation(self, *args):
        try:
            kwargs = {
                        "u": "(" + self.widgets["txt_field_A0"].text + ") * 1 + (" +
                             self.widgets["txt_field_A1"].text + ") * x + (" +
                             self.widgets["txt_field_A2"].text + ") * y + (" +
                             self.widgets["txt_field_A3"].text + ") * z",
                        "v": "z",
                        "a": float(self.widgets["txt_field_a"].text),
                        "b": float(self.widgets["txt_field_b"].text),
                        "ya": float(self.widgets["txt_field_y_a"].text),
                        "yb": float(self.widgets["txt_field_y_b"].text)
                    }
        except:
            return None
        points = FiringMethod(
            kwargs["u"],
            kwargs["v"],
            kwargs["a"],
            kwargs["b"],
            kwargs["ya"],
            kwargs["yb"]
        ).get_points()
        if points is not None:
            add_points_set(points)
