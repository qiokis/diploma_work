import tkinter as tk
import options as o


class AnalyticalIndicators(tk.LabelFrame):
    """
    Frame for analytical indicators
    """

    width = o.FIELD_WIDTH

    def __init__(self, root):
        super().__init__(root)
        self.configure(text="Аналитика")

        tk.Label(self, text="Мат. ожидание", width=self.width).grid(row=8, column=0, padx=5, pady=5)
        tk.Label(self, text="Дисперсия", width=self.width).grid(row=8, column=1, padx=5, pady=5)
        self.math_exp = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.dispersion = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.dispersion.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Станд. отклонение", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Коэф. вариации", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.stand_dev = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.var_coef = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.var_coef.grid(row=11, column=1, padx=5, pady=5)
        tk.Label(self, text="X гамма", width=self.width).grid(row=12, column=0, padx=5, pady=5)
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

    def clear(self):
        """
        Method clears indicators
        :return:
        """
        self.math_exp["text"] = ""
        self.dispersion["text"] = ""
        self.stand_dev["text"] = ""
        self.var_coef["text"] = ""
        self.gamma["text"] = ""

