from gui.main_frame import MainFrame
from calculations.calculator import Calculator
from handler.validator import Validator


class MainController:
    """
    Class mediator between gui, calculator logic and handler
    """

    def __init__(self, gui_comp: MainFrame):
        self.gui_comp = gui_comp
        self.calculator = Calculator()
        self.validator = Validator()
        cmnd = lambda x=True: self.validate_data(x)
        self.gui_comp.input_left.confirm.configure(command=cmnd)
        cmnd = lambda x=False: self.validate_data(x)
        self.gui_comp.input_right.confirm.configure(command=cmnd)

    def validate_data(self, state):
        """
        Method validates data from gui
        :param state: state for define what panel of gui is gives data
        :return:
        """
        if state:
            is_valid = self.validator.validate(self.gui_comp.input_left.get_data())
        else:
            is_valid = self.validator.validate(self.gui_comp.input_right.get_data())
        self.calculate_data(state, is_valid)

    def calculate_data(self, state, is_valid):
        """
        Method delegate calculations to Calculator and send them into gui
        :param state: state for define what panel of gui is gives data
        :param is_valid: results of validation
        :return:
        """
        if is_valid:
            if state:
                # Left panel (c is specified)
                values = {key: float(value) for key, value in self.gui_comp.input_left.get_data().items()}
                self.calculator.data_entry(values["a"], values["b"], values["c"], gamma=0.9)
                self.calculator.calculate_statistical()
                self.calculator.calculate_analytical()
                self.gui_comp.left_stat.set_data(self.calculator.get_indicators())
                self.gui_comp.left_analyt.set_data(self.calculator.get_indicators())
            else:
                # Right panel (c is not specified)
                values = {key: float(value) for key, value in self.gui_comp.input_right.get_data().items()}
                self.calculator.data_entry(values["a"], values["b"], c_avg=values["c_avg"], kc=values["kc"], gamma=0.9)
                self.calculator.calculate_statistical()
                self.gui_comp.right_stat.set_data(self.calculator.get_indicators())
