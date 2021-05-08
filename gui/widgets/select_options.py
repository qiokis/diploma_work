import options as o
import tkinter as tk


class SelectOptions(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.title("Настройки выборки")
        tk.Label(self, text="Количество интервалов (J)").pack(padx=5, pady=5)
        self.j_field = tk.Entry(self, width=o.FIELD_WIDTH)
        self.j_field.pack(padx=5, pady=5)
        tk.Label(self, text="Количество элементов выборки (n)").pack(padx=5, pady=5)
        self.n_field = tk.Entry(self, width=o.FIELD_WIDTH)
        self.n_field.pack(padx=5, pady=5)
        self.confirm = tk.Button(self, text="Подтвердить")
        self.confirm.pack(padx=5, pady=5)