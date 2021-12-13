from Code.GUI.GUIBuilder import GUIBuilder
from functools import partial
from Code.Graph.Graph import Graph
from Code.PointsKeeper.PointsKeeper import clear_points_sets


class GUILogicBuilder:
    @staticmethod
    def form_grid_with_main_equation():
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 11
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 80
        txt_field_A0 = GUIBuilder.my_text_field()
        txt_field_A1 = GUIBuilder.my_text_field()
        txt_field_A2 = GUIBuilder.my_text_field()
        txt_field_A3 = GUIBuilder.my_text_field()

        label_1 = GUIBuilder.my_label()
        label_x = GUIBuilder.my_label()
        label_y = GUIBuilder.my_label()
        label_y_y = GUIBuilder.my_label()
        label_y_y_y = GUIBuilder.my_label()

        label_1.text = "* 1 + "
        label_x.text = "* x + "
        label_y.text = "* y + "
        label_y_y.text = "* y'"
        label_y_y_y.text = "y'' = "

        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(label_y_y_y)
        grid.add_widget(txt_field_A0)
        grid.add_widget(label_1)
        grid.add_widget(txt_field_A1)
        grid.add_widget(label_x)
        grid.add_widget(txt_field_A2)
        grid.add_widget(label_y)
        grid.add_widget(txt_field_A3)
        grid.add_widget(label_y_y)
        return grid

    @staticmethod
    def form_main_cont():
        main_cont = GUIBuilder.my_grid_layout()
        main_cont.cols = 1
        main_cont.rows = None

        card = GUIBuilder.my_card()
        box1 = GUIBuilder.my_box_layout()
        box1.size_hint_y = .8
        box1.pos_hint = {"top": 1}
        graph = Graph()
        box1.add_widget(graph)
        card.add_widget(GUILogicBuilder.form_grid_with_main_equation())
        card.add_widget(GUILogicBuilder.form_logic_fields(graph.update_plt))
        card.add_widget(box1)
        main_cont.add_widget(card)
        return main_cont

    @staticmethod
    def form_boundary_cont():
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 8
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60

        label_y = GUIBuilder.my_label()
        label_equals = GUIBuilder.my_label()
        txt_field_x = GUIBuilder.my_text_field()
        txt_field_x.width = 80
        txt_field_x.input_filter = "float"
        txt_field_y = GUIBuilder.my_text_field()
        txt_field_y.width = 80
        txt_field_y.input_filter = "float"

        label_y.width = 32
        label_equals.width = 32
        label_y.text = 'y('
        label_equals.text = ') = '

        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(label_y)
        grid.add_widget(txt_field_x)
        grid.add_widget(label_equals)
        grid.add_widget(txt_field_y)
        return grid

    @staticmethod
    def form_logic_fields(graph_update_func):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 2
        grid.rows = None
        grid.padding = 40

        grid.size_hint_y = None
        grid.height = 250

        grid_first = GUIBuilder.my_grid_layout()
        grid_first.cols = 1
        grid_first.rows = 2

        grid_first.size_hint_y = None
        grid_first.height = 250

        first_boundary_cont = GUILogicBuilder.form_boundary_cont()
        second_boundary_cont = GUILogicBuilder.form_boundary_cont()
        print(first_boundary_cont.children)
        grid_first.add_widget(first_boundary_cont)
        grid_first.add_widget(second_boundary_cont)

        grid.add_widget(grid_first)
        grid.add_widget(GUILogicBuilder.form_import_export_clear_update_calculate(
            partial(print, "1"),
            partial(print, "2"),
            graph_update_func,
            clear_points_sets,
            partial(print, "4"))
        )
        return grid

    @staticmethod
    def form_import_export_clear_update_calculate(
            import_func,
            export_func,
            graph_update_func,
            clear_points_func,
            calculate_func
    ):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 1
        grid.rows = 3

        grid.size_hint_y = None
        grid.height = 250

        grid.add_widget(GUILogicBuilder.get_import_export_btn(import_func, export_func))
        grid.add_widget(GUILogicBuilder.get_clear_update_btn(graph_update_func, clear_points_func))
        grid.add_widget(GUILogicBuilder.get_calculate_btn(calculate_func))
        return grid

    @staticmethod
    def get_import_export_btn(import_func, export_func):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 2
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60
        grid.spacing = 15

        btn_import = GUIBuilder.my_button()
        btn_import.text = "Импортировать набор точек (CSV)"
        btn_import.bind(on_press=import_func)

        btn_export = GUIBuilder.my_button()
        btn_export.text = "Экспортировать набор точек (CSV)"
        btn_export.bind(on_press=export_func)

        grid.add_widget(btn_import)
        grid.add_widget(btn_export)
        return grid

    @staticmethod
    def get_clear_update_btn(graph_update_func, clear_points_func):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 2
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60
        grid.spacing = 15

        btn_clear = GUIBuilder.my_button()
        btn_clear.text = "Очистить холст"
        btn_clear.bind(on_press=clear_points_func)

        btn_update = GUIBuilder.my_button()
        btn_update.text = "Обновить холст"
        btn_update.bind(on_press=graph_update_func)

        grid.add_widget(btn_clear)
        grid.add_widget(btn_update)
        return grid

    @staticmethod
    def get_calculate_btn(calculate_func):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 1
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60

        btn = GUIBuilder.my_button()
        btn.text = "Решить краевую задачу"
        btn.bind(on_press=calculate_func)

        grid.add_widget(btn)
        return grid