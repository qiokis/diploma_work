import tkinter as tk
from gui.widgets.analytical_indicators import AnalyticalIndicators
from gui.widgets.statistical_indicators import StatisticalIndicators


class OutputFrame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        # c is specified
        self.c_spec_frame = tk.LabelFrame(self, text="c is specified")
        self.c_spec_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.left_stat_ind = StatisticalIndicators(self.c_spec_frame)
        self.left_stat_ind.pack(padx=10, pady=10)
        self.analyt_ind = AnalyticalIndicators(self.c_spec_frame)
        self.analyt_ind.pack(padx=10, pady=10)

        # c is not specified
        self.c_not_spec_frame = tk.LabelFrame(self, text="c is not specified")
        self.c_not_spec_frame.pack(padx=10, pady=10, fill=tk.Y, side=tk.RIGHT)
        self.right_stat_ind = StatisticalIndicators(self.c_not_spec_frame)
        self.right_stat_ind.pack(padx=10, pady=10)

