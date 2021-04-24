import tkinter as tk
import statistical_indicators
import analytical_indicators


class InputFrame(tk.Frame):

    width = 20

    def __init__(self, parent, c_spec=True):
        super().__init__()
        self.parent = parent

        tk.Label(self, text="Indicator a", width=self.width).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Indicator b", width=self.width).grid(row=0, column=1, padx=5, pady=5)
        self.a_field = tk.Entry(self, width=self.width)
        self.a_field.grid(row=1, column=0, padx=5, pady=5)
        self.a_field.bind("<FocusOut>", self.test)
        self.b_field = tk.Entry(self, width=self.width)
        self.b_field.grid(row=1, column=1, padx=5, pady=5)
        if c_spec:
            tk.Label(self, text="Indicator c", width=self.width).grid(row=4, column=0, padx=5, pady=5)
            self.c_field = tk.Entry(self, width=self.width)
            self.c_field.grid(row=5, column=0, padx=5, pady=5)
        else:
            tk.Label(self, text="Indicator c_avg", width=self.width).grid(row=4, column=0, padx=5, pady=5)
            self.c_avg_field = tk.Entry(self, width=self.width)
            self.c_avg_field.grid(row=5, column=0, padx=5, pady=5)
            tk.Label(self, text="Indicator kc", width=self.width).grid(row=4, column=1, padx=5, pady=5)
            self.kc_field = tk.Entry(self, width=self.width)
            self.kc_field.grid(row=5, column=1, padx=5, pady=5)


        tk.Button(self, text="Calculate", command=self.calculate).grid(row=6, column=0, columnspan=3, padx=5, pady=5)


    def calculate(self):
        pass
    #     if self.c_state.get():
    #         self.models.append(Model(a=float(self.a_field.get()),
    #                                  b=float(self.b_field.get()),
    #                                  n=10000,
    #                                  c=float(self.c_field.get())))
    #     else:
    #         self.models.append(Model(a=float(self.a_field.get()),
    #                                  b=float(self.b_field.get()),
    #                                  n=10000,
    #                                  kc=float(self.kc_field.get()),
    #                                  c_avg=float(self.c_avg_field.get())))
    #     self.destroy()
    #     stats_frame.StatsFrame(self.parent, self.models[0])

    def test(self, event):
        print("Working")

if __name__ == '__main__':
    root = tk.Tk()
    InputFrame(root, False).pack()
    root.mainloop()