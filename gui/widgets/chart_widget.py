import tkinter as tk
import matplotlib.pyplot as plt


class ChartWidget(tk.Frame):

    def __init__(self, root, selection, params):
        super().__init__(root)
        self.fig, self.ax = plt.subplots()
        self.ax.plot([i for i in range(len(selection))], selection, **params)
        self.ax.legend()
        plt.show()