from gui.main_frame import MainFrame
from calculations.calculator import Calculator


class MainController:

    def __init__(self, gui_comp: MainFrame):
        self.gui_comp = gui_comp
        self.calcul = Calculator()
        cmnd = lambda x=True: self.calculate(x)
        self.gui_comp.input_left.confirm.configure(command=cmnd)
        cmnd = lambda x=False: self.calculate(x)
        self.gui_comp.input_right.confirm.configure(command=cmnd)

    def calculate(self, state):
        if state:
            print(self.gui_comp.input_left.get_data())
        else:
            print(self.gui_comp.input_right.get_data())

