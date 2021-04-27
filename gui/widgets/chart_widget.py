import tkinter as tk
import matplotlib.pyplot as plt


class ChartWidget(tk.Frame):

    COLORS = ["red", "blue"]

    def __init__(self, root, selections, params):
        super().__init__(root)
        self.fig, self.ax = plt.subplots()
        for i in range(len(selections)):
            self.ax.plot([i for i in range(len(selections[i]))], selections[i], color=self.COLORS[i], **params[i])
        self.ax.legend()
        plt.show()