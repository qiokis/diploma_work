import tkinter as tk
from gui.statistical_indicators import StatisticalIndicators
from gui.input_frame import InputFrame
from gui.analytical_indicators import AnalyticalIndicators


class MainFrame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.c_spec_frame = tk.LabelFrame(self, text="c is specified")
        self.c_spec_frame.pack(side=tk.LEFT, padx=10)

        self.input_left = InputFrame(self.c_spec_frame)
        self.input_left.pack()
        self.left_analyt = AnalyticalIndicators(self.c_spec_frame)
        self.left_analyt.pack(pady=5)
        self.left_stat = StatisticalIndicators(self.c_spec_frame)
        self.left_stat.pack(pady=5)

        self.c_not_spec_frame = tk.LabelFrame(self, text="c is not specified")
        self.c_not_spec_frame.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

        self.input_right = InputFrame(self.c_not_spec_frame, False)
        self.input_right.pack(pady=5)
        self.right_stat = StatisticalIndicators(self.c_not_spec_frame)
        self.right_stat.pack(pady=5)




if __name__ == '__main__':
    root = tk.Tk()
    MainFrame(root).pack()
    root.mainloop()