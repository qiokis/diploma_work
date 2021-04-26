import tkinter as tk


class InputFrame(tk.LabelFrame):
    """
    Frame with entry fields for input data
    """

    width = 20

    def __init__(self, root, c_spec=True):
        super().__init__(root)
        self.configure(text="Input")
        self.c_spec = c_spec

        tk.Label(self, text="Indicator a", width=self.width).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Indicator b", width=self.width).grid(row=0, column=1, padx=5, pady=5)
        self.a_field = tk.Entry(self, width=self.width)
        self.a_field.grid(row=1, column=0, padx=5, pady=5)
        self.b_field = tk.Entry(self, width=self.width)
        self.b_field.grid(row=1, column=1, padx=5, pady=5)
        if self.c_spec:
            tk.Label(self, text="Indicator c", width=self.width).grid(row=4, column=0, padx=5, pady=5)
            self.c_field = tk.Entry(self, width=self.width)
            self.c_field.grid(row=5, column=0, padx=5, pady=5)
            tk.Label(self, text="Gamma", width=self.width).grid(row=4, column=1, padx=5, pady=5)
            self.gamma_field = tk.Entry(self, width=self.width)
            self.gamma_field.grid(row=5, column=1, padx=5, pady=5)
        else:
            tk.Label(self, text="Indicator c_avg", width=self.width).grid(row=4, column=0, padx=5, pady=5)
            self.c_avg_field = tk.Entry(self, width=self.width)
            self.c_avg_field.grid(row=5, column=0, padx=5, pady=5)
            tk.Label(self, text="Indicator kc", width=self.width).grid(row=4, column=1, padx=5, pady=5)
            self.kc_field = tk.Entry(self, width=self.width)
            self.kc_field.grid(row=5, column=1, padx=5, pady=5)
            tk.Label(self, text="Gamma", width=self.width).grid(row=6, column=0, padx=5, pady=5)
            self.gamma_field = tk.Entry(self, width=self.width)
            self.gamma_field.grid(row=7, column=0, padx=5, pady=5)

    def get_data(self):
        """
        Method returns data from fields
        :return: data
        """
        if self.c_spec:
            return {"a": self.a_field.get(),
                    "b": self.b_field.get(),
                    "c": self.c_field.get(),
                    "gamma": self.gamma_field.get()}
        else:
            return {"a": self.a_field.get(),
                    "b": self.b_field.get(),
                    "c_avg": self.c_avg_field.get(),
                    "kc": self.kc_field.get(),
                    "gamma": self.gamma_field.get()}