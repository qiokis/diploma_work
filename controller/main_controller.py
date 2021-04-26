from gui.input_frame import InputFrame
from gui.output_frame import OutputFrame
from calculations.calculator import Calculator
from handler.validator import Validator
from tkinter import messagebox as mb
import options as o


class MainController:
    """
    Class mediator between gui, calculator logic and handler
    """

    def __init__(self, root):

        self.root = root
        self.root.geometry(f"{o.WINDOW_WIDTH}x{o.WINDOWH_HEIGHT}")
        self.calculator = Calculator()
        self.validator = Validator()

        # InputFrame
        self.inp_frame = InputFrame(self.root)
        self.inp_frame.pack()
        # OutputFrame
        self.out_frame = OutputFrame(self.root)
        cmnd = lambda x=self.inp_frame: self.change_frame(x)
        self.out_frame.to_input.configure(command=cmnd)

        self.current_frame = self.inp_frame
        cmnd = lambda x=self.inp_frame: self.validate_data(x)
        self.inp_frame.confirm.configure(command=cmnd)

    def change_frame(self, frame):
        self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack()

    def validate_data(self, gui_comp):
        """
        Method validates data from gui
        :param gui_comp: gui component which gives data (input frame for this case)
        :return:
        """
        # c is specified
        is_valid_left = self.validator.validate(gui_comp.input_left.get_data())
        # c is not specified
        is_valid_right = self.validator.validate(gui_comp.input_right.get_data())
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
        values = self.validator.comma_replace(gui_comp.input_left.get_data())
        values = {key: float(value) for key, value in values.items()}
        self.calculator.data_entry(values["a"], values["b"], values["c"], gamma=values["gamma"])
        self.calculator.calculate_statistical()
        # set data to statistical indicators widget (c is specified) on output frame
        self.out_frame.left_stat_ind.set_data(self.calculator.indicator.indicators)
        self.calculator.calculate_analytical()
        # set data to analytical indicators widget on output frame
        self.out_frame.analyt_ind.set_data(self.calculator.indicator.indicators)

    def calculate_right_widget(self, gui_comp):
        """
        Method for calculate indicators for input widget where c is not specified
        :param gui_comp: input frame
        :return:
        """
        # Right panel (c is not specified)
        values = self.validator.comma_replace(gui_comp.input_right.get_data())
        values = {key: float(value) for key, value in values.items()}
        self.calculator.data_entry(values["a"], values["b"], c_avg=values["c_avg"],
                                   kc=values["kc"], gamma=values["gamma"])
        self.calculator.calculate_statistical()
        # set data to statistical indicators widget (c is not specified) on output frame
        self.out_frame.right_stat_ind.set_data(self.calculator.indicator.indicators)

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
        self.change_frame(self.out_frame)

    def set_data(self, gui_comp):
        pass
