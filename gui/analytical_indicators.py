import tkinter as tk


class AnalyticalIndicators(tk.Frame):

    width = 20

    def __init__(self, root):
        super().__init__(root)

        tk.Label(self, text="Analytical", width=self.width).grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        tk.Label(self, text="Math expectation", width=self.width).grid(row=8, column=0, padx=5, pady=5)
        tk.Label(self, text="Dispersion", width=self.width).grid(row=8, column=1, padx=5, pady=5)
        self.math_exp = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.dispersion = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.dispersion.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Standard deviation", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Variation coefficient", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.stand_dev = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.var_coef = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.var_coef.grid(row=11, column=1, padx=5, pady=5)
        tk.Label(self, text="Standard deviation", width=self.width).grid(row=12, column=0, padx=5, pady=5)
        self.gamma = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.gamma.grid(row=13, column=0, padx=5, pady=5)
