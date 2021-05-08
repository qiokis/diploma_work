from gui.frames.input_frame import InputFrame
from gui.frames.output_frame import OutputFrame
from calculations.calculator import Calculator
from handler.validator import Validator
import options as o
from gui.widgets.chart_widget import ChartWidget
from gui.widgets.select_options import SelectOptions

from tkinter import messagebox as mb


class MainController:
    """
    Class mediator between gui, calculator logic and handler
    """
    # Количество интервалов
    J = 44
    n = 10000

    def __init__(self, root):

        self.__root = root
        self.__root.title("Оценка ПНРС")
        self.__root.geometry(f"{o.WINDOW_WIDTH}x{o.WINDOWH_HEIGHT}")
        self.__root.resizable(False, False)
        self.__calculator = Calculator()
        self.__validator = Validator()

        # Настройки выборки
        self.options = SelectOptions(self.__root)
        self.options.withdraw()
        self.options.confirm.configure(command=self.setup_options)
        self.options.protocol("WM_DELETE_WINDOW", self.setup_options)

        # InputFrame
        self.__inp_frame = InputFrame(self.__root)
        self.__inp_frame.pack()

        self.__current_frame = self.__inp_frame
        cmnd = lambda x=self.__inp_frame: self.validate_data(x)
        self.__inp_frame.confirm.configure(command=cmnd)
        self.__inp_frame.options.configure(command=self.options.deiconify)

        # Left = c is specified
        self.__left_arrays = {"uzli": [], "counts": [], "m": [], "k": []}
        # Right = c is not specified
        self.__right_arrays = {"uzli": [], "counts": [], "m": [], "k": []}

        # OutputFrame
        self.__out_frame = OutputFrame(self.__root)
        cmnd = lambda x=self.__inp_frame: self.change_frame(x)
        self.__out_frame.to_input.configure(command=self.change_to_input)
        cmnd = lambda x="counts": self.create_chart(x)
        self.__out_frame.to_chart_counts.configure(command=cmnd)
        cmnd = lambda x="k": self.create_chart(x)
        self.__out_frame.to_chart_k.configure(command=cmnd)
        cmnd = lambda x="m": self.create_chart(x)
        self.__out_frame.to_chart_m.configure(command=cmnd)

    def setup_options(self):
        try:
            self.J = int(self.options.j_field.get())
        except ValueError as e:
            pass
        try:
            self.n = int(self.options.n_field.get())
        except ValueError as e:
            pass
        self.options.withdraw()

    def change_frame(self, frame):
        """
        Method changes current frame
        :param frame: the frame to switch to
        :return:
        """
        self.__current_frame.pack_forget()
        self.__current_frame = frame
        self.__current_frame.pack()

    def change_to_input(self):
        """
        Method changes current frame to start frame (input frame) and clears all data
        :return:
        """
        self.__current_frame.pack_forget()
        self.__current_frame = self.__inp_frame
        self.__current_frame.pack()
        self.__out_frame.clear()
        # Left = c is specified
        self.__left_arrays = {"uzli": [], "counts": [], "m": [], "k": []}
        # Right = c is not specified
        self.__right_arrays = {"uzli": [], "counts": [], "m": [], "k": []}

    def validate_data(self, gui_comp):
        """
        Method validates data from gui
        :param gui_comp: gui component which gives data (input frame for this case)
        :return:
        """
        # c is specified
        is_valid_left = self.__validator.validate(gui_comp.input_left.get_data())
        # c is not specified
        is_valid_right = self.__validator.validate(gui_comp.input_right.get_data())
        ans = 0
        if all((is_valid_right, is_valid_left)):
            # both widgets data are valid
            ans = 2
        elif any((is_valid_right, is_valid_left)):
            # one widget data are valid
            if mb.askokcancel("Warning", "One of the models is not filled up, you want to continue?"):
                ans = 1
        elif not all((is_valid_right, is_valid_left)):
            # both widgets data are not valid
            mb.showerror("Error", "Both models is not filled up!")
            ans = 0
        if ans:
            self.calculate_data(ans, gui_comp, {"left": is_valid_left, "right": is_valid_right})

    def calculate_left_widget(self, gui_comp):
        """
        Method for calculate indicators for input widget where c is specified
        :param gui_comp: input frame
        :return:
        """
        # Left panel (c is specified)
        values = self.__validator.comma_replace(gui_comp.input_left.get_data())
        values = {key: float(value) for key, value in values.items()}
        self.__calculator.data_entry(values["a"], values["b"], values["c"], gamma=values["gamma"], n=self.n)
        self.__calculator.calculate_statistical(self.n)
        self.__left_arrays = self.__calculator.select.create_arrays(self.J, values["gamma"])
        self.__calculator.indicator.set_xrs({"xr": self.__calculator.to_fixed(self.__left_arrays["xr"]),
                                           "xr_gamma": self.__calculator.to_fixed(self.__left_arrays["xr_gamma"])})

        # set data to statistical indicators widget (c is specified) on output frame
        self.__out_frame.left_stat_ind.set_data(self.__calculator.indicator.indicators)
        self.__calculator.calculate_analytical()
        # set data to analytical indicators widget on output frame
        self.__out_frame.analyt_ind.set_data(self.__calculator.indicator.indicators)

    def calculate_right_widget(self, gui_comp):
        """
        Method for calculate indicators for input widget where c is not specified
        :param gui_comp: input frame
        :return:
        """
        # Right panel (c is not specified)
        values = self.__validator.comma_replace(gui_comp.input_right.get_data())
        values = {key: float(value) for key, value in values.items()}
        self.__calculator.data_entry(values["a"], values["b"], c_avg=values["c_avg"],
                                     kc=values["kc"], gamma=values["gamma"], n=self.n)
        self.__calculator.calculate_statistical(self.n)
        self.__right_arrays = self.__calculator.select.create_arrays(self.J, values["gamma"])
        self.__calculator.indicator.set_xrs({"xr": self.__calculator.to_fixed(self.__right_arrays["xr"]),
                                           "xr_gamma": self.__calculator.to_fixed(self.__right_arrays["xr_gamma"])})
        # set data to statistical indicators widget (c is not specified) on output frame
        self.__out_frame.right_stat_ind.set_data(self.__calculator.indicator.indicators)

    def calculate_data(self, ans, gui_comp, valid):
        """
        Method delegate calculations to Calculator and send them into gui
        :param valid: states of validation for both widgets
        :param ans: how much widgets are ready for calculations
        :param gui_comp: gui component which gives data (input frame for this case)
        :return:
        """
        if ans == 2:
            # Left panel (c is specified)
            self.calculate_left_widget(gui_comp)
            # Right panel (c is not specified)
            self.calculate_right_widget(gui_comp)

        elif ans == 1:
            if valid["left"]:
                # Left panel (c is specified)
                self.calculate_left_widget(gui_comp)
            else:
                # Right panel (c is not specified)
                self.calculate_right_widget(gui_comp)
        self.change_frame(self.__out_frame)

    def create_chart(self, chart_type):
        """
        Method creates charts
        :param chart_type: type of chart
        :return:
        """
        ChartWidget(self.__root, (self.__left_arrays[chart_type], self.__right_arrays[chart_type]),
                    ({"label": "c is specified"}, {"label": "c is not specified"}))

