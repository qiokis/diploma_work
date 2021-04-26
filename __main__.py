__author__ = "qiokis"

if __name__ == '__main__':
    import tkinter as tk
    from gui.input_frame import InputFrame
    from controller.main_controller import MainController

    root = tk.Tk()
    MainController(root)
    root.mainloop()
