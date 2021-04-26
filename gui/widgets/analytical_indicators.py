import tkinter as tk


class AnalyticalIndicators(tk.LabelFrame):
    """
    Frame for analytical indicators
    """

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
        tk.Label(self, text="X gamma", width=self.width).grid(row=12, column=0, padx=5, pady=5)
        self.gamma = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.gamma.grid(row=13, column=0, padx=5, pady=5)

    def set_data(self, values: dict):
        """
        Method records data to frame
        :param values: data from calculator
        :return:
        """
        self.math_exp["text"] = values["Analytical"]["Math expectation"]
        self.dispersion["text"] = values["Analytical"]["Dispersion"]
        self.stand_dev["text"] = values["Analytical"]["Standard Deviation"]
        self.var_coef["text"] = values["Analytical"]["Variation coefficient"]
        self.gamma["text"] = values["Analytical"]["X gamma"]

