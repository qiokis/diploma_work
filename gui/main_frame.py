import tkinter as tk
import analytical_indicators
import input_frame
import statistical_indicators


class MainFrame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.c_spec_frame = tk.LabelFrame(self, text="c is specified")
        self.c_spec_frame.pack(side=tk.LEFT, padx=10)

        input_frame.InputFrame(self.c_spec_frame).pack()
        analytical_indicators.AnalyticalIndicators(self.c_spec_frame).pack(pady=5)
        statistical_indicators.StatisticalIndicators(self.c_spec_frame).pack(pady=5)

        self.c_not_spec_frame = tk.LabelFrame(self, text="c is not specified")
        self.c_not_spec_frame.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

        input_frame.InputFrame(self.c_not_spec_frame, False).pack(pady=5)
        statistical_indicators.StatisticalIndicators(self.c_not_spec_frame).pack(pady=5)




if __name__ == '__main__':
    root = tk.Tk()
    MainFrame(root).pack()
    root.mainloop()