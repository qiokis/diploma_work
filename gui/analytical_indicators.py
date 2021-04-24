import tkinter as tk


class AnalyticalIndicators(tk.LabelFrame):

    width = 20

    def __init__(self, root):
        super().__init__(root)
        self.configure(text="Analytical")

        tk.Label(self, text="Math expectation", width=self.width).grid(row=8, column=0, padx=5, pady=5)
        tk.Label(self, text="Dispersion", width=self.width).grid(row=8, column=1, padx=5, pady=5)
        self.math_exp = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.dispersion = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.dispersion.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Standard deviation", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Variation coefficient", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.stand_dev = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.var_coef = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.var_coef.grid(row=11, column=1, padx=5, pady=5)
        tk.Label(self, text="Standard deviation", width=self.width).grid(row=12, column=0, padx=5, pady=5)
        self.gamma = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.gamma.grid(row=13, column=0, padx=5, pady=5)
