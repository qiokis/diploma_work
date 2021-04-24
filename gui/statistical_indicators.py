import tkinter as tk


class StatisticalIndicators(tk.LabelFrame):

    width = 20

    def __init__(self, root):
        super().__init__(root)
        self.configure(text="Statistical")

        tk.Label(self, text="Math expectation", width=self.width).grid(row=8, column=0, padx=5, pady=5)
        tk.Label(self, text="Dispersion", width=self.width).grid(row=8, column=1, padx=5, pady=5)
        self.math_exp = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.dispersion = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.dispersion.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Standard deviation", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Delta", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.stand_dev = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.delta = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.delta.grid(row=11, column=1, padx=5, pady=5)
