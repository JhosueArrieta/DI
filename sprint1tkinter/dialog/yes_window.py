#importamos tkinter y le ponemos un alias mas pequeño
import tkinter as tk
#este ns mut bn que es pero sirve para crear la etiqueta
from tkinter import ttk
#creamos una funcion que pasaremos a window.py para la acción al clicar el botón
def show_yes_window(): 
    #con esto creamos la ventana que se va abrir al pulsar el boton
    yes_root =tk.Tk()
    #le asignamos un titulo a la ventana
    yes_root.title("VENTANA SÍ")
    #creamos una etiqueta indicando el padre y la empaquetamos
    label = ttk.Label(yes_root,text = "Estas en la ventana si")
    label.pack()
    #permitimos poder cerrar la ventana creada anteriormente
    yes_root.mainloop()