#mostrar de manera libre una imagen, un label(título), y otro label de entre 100 y 200 caracteres a modo de descripción de la img
import tkinter as tk
from tkinter import ttk

def detail_window (cell):
    #explicacion de Carlos 
    root = tk.Toplevel()
    #añadimos las etiquetas correspondientes que pide el ejercicio
    label1 = ttk.Label(root, image=cell.Image_tk)
    label2 = ttk.Label(root, text=cell.name)
    label3 = ttk.Label(root, text=cell.desc)
    #empaquetamos las etiquetas
    label1.pack()
    label2.pack()
    label3.pack()
    #Ajustamos tamaños de las ventanas con las siguientes funciones
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    #cerramos bucle
    root.mainloop()
