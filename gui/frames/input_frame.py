import tkinter as tk
import options as o
from gui.widgets.input_widget import InputWidget


class InputFrame(tk.Frame):
    """
    Main frame which combines all functional frames and gives acces to them
    """

    def __init__(self, root):
        super().__init__(root)

        # c is specified
        self.__c_spec_frame = tk.LabelFrame(self, text="c is specified")
        self.__c_spec_frame.pack(padx=10, pady=10)
        self.input_left = InputWidget(self.__c_spec_frame)
        self.input_left.pack(padx=10, pady=10)

        # c is not specified
        self.__c_not_spec_frame = tk.LabelFrame(self, text="c is not specified")
        self.__c_not_spec_frame.pack(padx=10, pady=10)
        self.input_right = InputWidget(self.__c_not_spec_frame, False)
        self.input_right.pack(padx=10, pady=10)

        self.confirm = tk.Button(self, text="Рассчитать", width=o.FIELD_WIDTH)
        self.confirm.pack(padx=5, pady=5, side=tk.RIGHT)
        self.options = tk.Button(self, text="Настройки выборки", width=o.FIELD_WIDTH)
        self.options.pack(padx=5, pady=5)