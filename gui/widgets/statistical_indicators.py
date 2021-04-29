import tkinter as tk
import options as o


class StatisticalIndicators(tk.LabelFrame):
    """
    Frame for statistical indicators
    """
    # TODO добавить Xr, Доверительный интервал, Xrgamma
    width = o.FIELD_WIDTH

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
        tk.Label(self, text="Confidence interval", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.stand_dev = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.confidence_interval = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.confidence_interval.grid(row=11, column=1, padx=5, pady=5)

    def set_data(self, values: dict):
        """
        Method records data to frame
        :param values: data from calculator
        :return:
        """
        self.math_exp["text"] = values["Statistical"]["Math expectation"]
        self.dispersion["text"] = values["Statistical"]["Dispersion"]
        self.stand_dev["text"] = values["Statistical"]["Standard Deviation"]
        self.confidence_interval["text"] = values["Statistical"]["Conf int"]

    def clear(self):
        self.math_exp["text"] = ""
        self.dispersion["text"] = ""
        self.stand_dev["text"] = ""
        self.confidence_interval["text"] = ""
