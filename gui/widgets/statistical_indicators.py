import tkinter as tk
import options as o


class StatisticalIndicators(tk.LabelFrame):
    """
    Frame for statistical indicators
    """
    width = o.FIELD_WIDTH

    def __init__(self, root):
        super().__init__(root)
        self.configure(text="Статистика")

        tk.Label(self, text="Мат. ожидание", width=self.width).grid(row=8, column=0, padx=5, pady=5)
        tk.Label(self, text="Xr", width=self.width).grid(row=8, column=1, padx=5, pady=5)
        self.__math_exp = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.__xr = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__xr.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Станд. отклонение", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Дов. интверал", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.__stand_dev = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.__confidence_interval = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__confidence_interval.grid(row=11, column=1, padx=5, pady=5)
        tk.Label(self, text="Xr gamma", width=self.width).grid(row=12, column=0, padx=5, pady=5)
        self.__xr_gamma = tk.Label(self, width=self.width, relief="sunken", bg="white", bd=1)
        self.__xr_gamma.grid(row=13, column=0, padx=5, pady=5)

    def set_data(self, values: dict):
        """
        Method records data to frame
        :param values: data from calculator
        :return:
        """
        self.__math_exp["text"] = values["Statistical"]["Math expectation"]
        self.__xr["text"] = values["Statistical"]["Xr"]
        self.__xr_gamma["text"] = values["Statistical"]["Xr gamma"]
        self.__stand_dev["text"] = values["Statistical"]["Standard Deviation"]
        self.__confidence_interval["text"] = values["Statistical"]["Conf int"]

    def clear(self):
        """
        Method clears indicators
        :return:
        """
        self.__math_exp["text"] = ""
        self.__xr["text"] = ""
        self.__stand_dev["text"] = ""
        self.__confidence_interval["text"] = ""
        self.__xr_gamma["text"] = ""
