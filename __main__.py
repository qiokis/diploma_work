__author__ = "qiokis"

if __name__ == '__main__':
    import tkinter as tk
    from gui.main_frame import MainFrame
    from controller.main_controller import MainController

    root = tk.Tk()
    m = MainFrame(root)
    m.pack()
    MainController(m)
    root.mainloop()
