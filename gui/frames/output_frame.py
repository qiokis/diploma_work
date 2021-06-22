import tkinter as tk
import options as o
from gui.widgets.analytical_indicators import AnalyticalIndicators
from gui.widgets.statistical_indicators import StatisticalIndicators


class OutputFrame(tk.Frame):
    """
    Frame responds for outputting calculated data
    """

    def __init__(self, root):
        super().__init__(root)

        self.__main_frame = tk.Frame(self)
        self.__main_frame.pack(side=tk.TOP)

        # c is specified
        self.__c_spec_frame = tk.LabelFrame(self.__main_frame, text="c is specified")
        self.__c_spec_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.left_stat_ind = StatisticalIndicators(self.__c_spec_frame)
        self.left_stat_ind.pack(padx=10, pady=10)
        self.analyt_ind = AnalyticalIndicators(self.__c_spec_frame)
        self.analyt_ind.pack(padx=10, pady=10)

        # c is not specified
        self.__c_not_spec_frame = tk.LabelFrame(self.__main_frame, text="c is not specified")
        self.__c_not_spec_frame.pack(padx=10, pady=10, fill=tk.Y, side=tk.RIGHT)
        self.right_stat_ind = StatisticalIndicators(self.__c_not_spec_frame)
        self.right_stat_ind.pack(padx=10, pady=10)

        self.__buttons = tk.Frame(self)
        self.__buttons.pack(fill=tk.Y, expand=True, anchor=tk.S)

        self.to_input = tk.Button(self.__buttons, text="Back to input", width=o.FIELD_WIDTH)
        self.to_input.pack(padx=5, pady=5, side=tk.LEFT)
        self.to_chart_counts = tk.Button(self.__buttons, text="To chart counts", width=o.FIELD_WIDTH)
        self.to_chart_counts.pack(padx=5, pady=5, side=tk.LEFT)
        self.to_chart_k = tk.Button(self.__buttons, text="To chart k", width=o.FIELD_WIDTH)
        self.to_chart_k.pack(padx=5, pady=5, side=tk.LEFT)
        self.to_chart_m = tk.Button(self.__buttons, text="To chart m", width=o.FIELD_WIDTH)
        self.to_chart_m.pack(padx=5, pady=5, side=tk.LEFT)

    def clear(self):
        """
        Method clears data from fields
        :return:
        """
        self.left_stat_ind.clear()
        self.right_stat_ind.clear()
        self.analyt_ind.clear()



