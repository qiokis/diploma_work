__author__ = "qiokis"

if __name__ == '__main__':
    import tkinter as tk
    from controllers.main_controller import MainController

    root = tk.Tk()
    MainController(root)
    root.mainloop()
