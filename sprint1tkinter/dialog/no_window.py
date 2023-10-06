#en este caso importo de tkinter tanto ttk como Tk; este ultimo para crear la ventana
from tkinter import ttk, Tk

def show_no_window(): 
    #creamos la instancia de la ventana para abrirse 
    no_root = Tk()
    #colocamos un título a la ventana
    no_root.title("VENTANA NO")
    #creamos etiqueta y la empaquetamos; indicamos padre siempre
    label = ttk.Label(no_root,text = "Estas en la ventana no")
    label.pack()
    #cerramos el bucle de la ventana para que pare de ejecutar
    no_root.mainloop()