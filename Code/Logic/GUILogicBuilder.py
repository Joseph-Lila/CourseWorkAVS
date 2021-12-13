from Code.GUI.GUIBuilder import GUIBuilder
from Code.Graph.Graph import Graph


class GUILogicBuilder:
    @staticmethod
    def form_grid_with_main_equation(widgets):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 11
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 80
        txt_field_A0 = GUIBuilder.my_text_field()
        txt_field_A1 = GUIBuilder.my_text_field()
        txt_field_A2 = GUIBuilder.my_text_field()
        txt_field_A3 = GUIBuilder.my_text_field()

        widgets["txt_field_A0"] = txt_field_A0
        widgets["txt_field_A1"] = txt_field_A1
        widgets["txt_field_A2"] = txt_field_A2
        widgets["txt_field_A3"] = txt_field_A3

        label_1 = GUIBuilder.my_label()
        label_x = GUIBuilder.my_label()
        label_y = GUIBuilder.my_label()
        label_y_y = GUIBuilder.my_label()
        label_y_y_y = GUIBuilder.my_label()

        widgets["label_1"] = label_1
        widgets["label_x"] = label_x
        widgets["label_y"] = label_y
        widgets["label_y_y"] = label_y_y
        widgets["label_y_y_y"] = label_y_y_y

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
        widgets = dict()
        main_cont = GUIBuilder.my_grid_layout()
        main_cont.cols = 1
        main_cont.rows = None

        card = GUIBuilder.my_card()
        box1 = GUIBuilder.my_box_layout()
        box1.size_hint_y = .8
        box1.pos_hint = {"top": 1}
        graph = Graph()
        widgets["graph"] = graph
        box1.add_widget(graph)
        card.add_widget(GUILogicBuilder.form_grid_with_main_equation(widgets))
        card.add_widget(GUILogicBuilder.form_logic_fields(widgets))
        card.add_widget(box1)
        main_cont.add_widget(card)
        return main_cont, widgets

    @staticmethod
    def form_boundary_cont():
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 8
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60

        label_c = GUIBuilder.my_label()
        label_y_c = GUIBuilder.my_label()
        txt_field_c = GUIBuilder.my_text_field()
        txt_field_c.width = 80
        txt_field_c.input_filter = "float"
        txt_field_y_c = GUIBuilder.my_text_field()
        txt_field_y_c.width = 80
        txt_field_y_c.input_filter = "float"

        label_c.width = 32
        label_y_c.width = 32
        label_c.text = 'y('
        label_y_c.text = ') = '

        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(GUIBuilder.my_widget())
        grid.add_widget(label_c)
        grid.add_widget(txt_field_c)
        grid.add_widget(label_y_c)
        grid.add_widget(txt_field_y_c)
        return grid

    @staticmethod
    def form_logic_fields(widgets):
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

        widgets["txt_field_y_a"] = first_boundary_cont.children[0]
        widgets["txt_field_a"] = first_boundary_cont.children[2]
        widgets["txt_field_y_b"] = second_boundary_cont.children[0]
        widgets["txt_field_b"] = second_boundary_cont.children[2]

        widgets["label_y_a"] = first_boundary_cont.children[1]
        widgets["label_a"] = first_boundary_cont.children[3]
        widgets["label_y_b"] = second_boundary_cont.children[1]
        widgets["label_b"] = second_boundary_cont.children[3]

        grid_first.add_widget(first_boundary_cont)
        grid_first.add_widget(second_boundary_cont)

        grid.add_widget(grid_first)
        grid.add_widget(GUILogicBuilder.form_import_export_clear_update_calculate(widgets))
        return grid

    @staticmethod
    def form_import_export_clear_update_calculate(widgets):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 1
        grid.rows = 3

        grid.size_hint_y = None
        grid.height = 250

        import_export_btn = GUILogicBuilder.get_import_export_btn(widgets)
        clear_update_btn = GUILogicBuilder.get_clear_update_btn(widgets)
        calculate_btn = GUILogicBuilder.get_calculate_btn(widgets)
        grid.add_widget(import_export_btn)
        grid.add_widget(clear_update_btn)
        grid.add_widget(calculate_btn)
        return grid

    @staticmethod
    def get_import_export_btn(widgets):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 2
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60
        grid.spacing = 15

        btn_import = GUIBuilder.my_button()
        btn_import.text = "Импортировать набор точек (CSV)"
        widgets["btn_import"] = btn_import

        btn_export = GUIBuilder.my_button()
        btn_export.text = "Экспортировать набор точек (CSV)"
        widgets["btn_export"] = btn_export

        grid.add_widget(btn_import)
        grid.add_widget(btn_export)
        return grid

    @staticmethod
    def get_clear_update_btn(widgets):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 2
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60
        grid.spacing = 15

        btn_clear = GUIBuilder.my_button()
        btn_clear.text = "Очистить холст"
        widgets["btn_clear"] = btn_clear

        btn_update = GUIBuilder.my_button()
        btn_update.text = "Обновить холст"
        widgets["btn_update"] = btn_update

        grid.add_widget(btn_clear)
        grid.add_widget(btn_update)
        return grid

    @staticmethod
    def get_calculate_btn(widgets):
        grid = GUIBuilder.my_grid_layout()
        grid.cols = 1
        grid.rows = None
        grid.size_hint_y = None
        grid.height = 60

        btn_calculate = GUIBuilder.my_button()
        btn_calculate.text = "Решить краевую задачу"
        widgets["btn_calculate"] = btn_calculate

        grid.add_widget(btn_calculate)
        return grid
