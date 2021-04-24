import tkinter as tk


class StatisticalIndicators(tk.Frame):

    width = 20

    def __init__(self, root):
        super().__init__(root)

        tk.Label(self, text="Statistical", width=self.width).grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        tk.Label(self, text="Math expectation", width=self.width).grid(row=8, column=0, padx=5, pady=5)
        tk.Label(self, text="Dispersion", width=self.width).grid(row=8, column=1, padx=5, pady=5)
        self.math_exp = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.math_exp.grid(row=9, column=0, padx=5, pady=5)
        self.dispersion = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.dispersion.grid(row=9, column=1, padx=5, pady=5)
        tk.Label(self, text="Standard deviation", width=self.width).grid(row=10, column=0, padx=5, pady=5)
        tk.Label(self, text="Delta", width=self.width).grid(row=10, column=1, padx=5, pady=5)
        self.stand_dev = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.stand_dev.grid(row=11, column=0, padx=5, pady=5)
        self.delta = tk.Entry(self, state=tk.DISABLED, width=self.width)
        self.delta.grid(row=11, column=1, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    StatisticalIndicators(root).pack()
    root.mainloop()