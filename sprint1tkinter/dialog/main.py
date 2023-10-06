from tkinter import Tk
from window import MainWindow

if __name__ == "__main__":
    #con esta linea permitimos abrir ventana 
    root = Tk()
    app = MainWindow(root)
    #con esta cerramos el ciclo de una ventana
    root.mainloop()

    