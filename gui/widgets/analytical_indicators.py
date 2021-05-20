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
        self.__math_exp = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.__dispersion = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__dispersion.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Станд. отклонение", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Коэф. вариации", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.__stand_dev = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.__var_coef = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__var_coef.grid(row=11, column=1, padx=5, pady=5)
        tk.Label(self, text="X gamma", width=self.width).grid(row=12, column=0, padx=5, pady=5)
        self.__gamma = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__gamma.grid(row=13, column=0, padx=5, pady=5)

    def set_data(self, values: dict):
        """
        Method records data to frame
        :param values: data from calculator
        :return:
        """
        self.__math_exp["text"] = values["Analytical"]["Math expectation"]
        self.__dispersion["text"] = values["Analytical"]["Dispersion"]
        self.__stand_dev["text"] = values["Analytical"]["Standard Deviation"]
        self.__var_coef["text"] = values["Analytical"]["Variation coefficient"]
        self.__gamma["text"] = values["Analytical"]["X gamma"]

    def clear(self):
        """
        Method clears indicators
        :return:
        """
        self.__math_exp["text"] = ""
        self.__dispersion["text"] = ""
        self.__stand_dev["text"] = ""
        self.__var_coef["text"] = ""
        self.__gamma["text"] = ""
