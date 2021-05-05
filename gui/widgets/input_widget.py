import tkinter as tk
import options as o


class InputWidget(tk.LabelFrame):
    """
    Frame with entry fields for input data
    """

    width = o.FIELD_WIDTH

    def __init__(self, root, c_spec=True):
        super().__init__(root)
        self.configure(text="Input")
        self.__c_spec = c_spec

        tk.Label(self, text="Indicator a", width=self.width).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Indicator b", width=self.width).grid(row=0, column=1, padx=5, pady=5)
        self.__a_field = tk.Entry(self, width=self.width)
        self.__a_field.grid(row=1, column=0, padx=5, pady=5)
        self.__b_field = tk.Entry(self, width=self.width)
        self.__b_field.grid(row=1, column=1, padx=5, pady=5)
        if self.__c_spec:
            tk.Label(self, text="Indicator c", width=self.width).grid(row=4, column=0, padx=5, pady=5)
            self.__c_field = tk.Entry(self, width=self.width)
            self.__c_field.grid(row=5, column=0, padx=5, pady=5)
            tk.Label(self, text="Gamma", width=self.width).grid(row=4, column=1, padx=5, pady=5)
            self.__gamma_field = tk.Entry(self, width=self.width)
            self.__gamma_field.grid(row=5, column=1, padx=5, pady=5)
        else:
            tk.Label(self, text="Indicator c_avg", width=self.width).grid(row=4, column=0, padx=5, pady=5)
            self.__c_avg_field = tk.Entry(self, width=self.width)
            self.__c_avg_field.grid(row=5, column=0, padx=5, pady=5)
            tk.Label(self, text="Indicator kc", width=self.width).grid(row=4, column=1, padx=5, pady=5)
            self.__kc_field = tk.Entry(self, width=self.width)
            self.__kc_field.grid(row=5, column=1, padx=5, pady=5)
            tk.Label(self, text="Gamma", width=self.width).grid(row=6, column=0, padx=5, pady=5)
            self.__gamma_field = tk.Entry(self, width=self.width)
            self.__gamma_field.grid(row=7, column=0, padx=5, pady=5)

    def get_data(self):
        """
        Method returns data from fields
        :return: data
        """
        if self.__c_spec:
            return {"a": self.__a_field.get(),
                    "b": self.__b_field.get(),
                    "c": self.__c_field.get(),
                    "gamma": self.__gamma_field.get()}
        else:
            return {"a": self.__a_field.get(),
                    "b": self.__b_field.get(),
                    "c_avg": self.__c_avg_field.get(),
                    "kc": self.__kc_field.get(),
                    "gamma": self.__gamma_field.get()}