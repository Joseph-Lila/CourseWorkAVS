from functools import partial
from Code.BoundaryValueProblem.FiringMethod import FiringMethod
from Code.PointsKeeper.PointsKeeper import clear_points_sets, add_points_set, points_set
from plyer import filechooser
from kivymd.toast import toast
import csv


class GUILogicBinder:
    def __init__(self, widgets):
        self.widgets = widgets
        self.functions = dict()
        self.params = dict()
        self.__form_functions()
        self.file_manager_answer = '?'

    def __form_functions(self):
        self.functions["btn_update"] = self.widgets["graph"].update_plt
        self.params["btn_update"] = []
        self.functions["btn_clear"] = clear_points_sets
        self.params["btn_clear"] = []
        self.functions["btn_calculate"] = self.send_points_after_calculation
        self.params["btn_calculate"] = []
        self.functions["btn_import"] = self.import_points
        self.params["btn_import"] = []
        self.functions["btn_export"] = self.export_points
        self.params["btn_export"] = []

    def bind_widgets(self):
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

    def choose_file_using_manager(self, *args):
        try:
            path = filechooser.open_file()[0]
        except:
            return False
        toast(path)
        self.file_manager_answer = path
        return True

    def import_points(self, *args):
        if self.choose_file_using_manager():
            outcome = [[], []]
            with open(self.file_manager_answer, "r") as f_obj:
                reader = csv.DictReader(f_obj, delimiter=';')
                for line in reader:
                    try:
                        outcome[0].append(float(line["x"]))
                        outcome[1].append(float(line["y"]))
                    except:
                        clear_points_sets()
                        return False
                        pass
                        # note
                clear_points_sets()
                add_points_set(outcome)
                return True

    def export_points(self, *args):
        if self.choose_file_using_manager():
            fieldnames = ["x", "y"]
            try:
                with open(self.file_manager_answer, "w") as f_obj:
                    writer = csv.DictWriter(f_obj, delimiter=';', fieldnames=fieldnames)
                    writer.writeheader()
                    set_ = points_set()[-1]
                    for i in range(len(set_[-1])):
                        writer.writerow({'x': set_[0][i], 'y': set_[1][i]})
                    return True
            except:
                return False
