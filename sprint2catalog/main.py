from tkinter import Tk
from window import MainWindow
from loading_window import loading

if __name__ == "__main__":
    root = Tk()
    #app = MainWindow(root)
    app = loading(root)
    root.mainloop()


    