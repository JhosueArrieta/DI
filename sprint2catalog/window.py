from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import detail_window
from PIL import Image, ImageTk
from detail_window import detail_window
from tkinter import messagebox

class MainWindow():
    #accion que se ejecuta al clicar en ayuda
    def onButtonClicked(self):
       messagebox.showinfo("Acerca del desarrollador","Messi, the best player in the world.")

    def __init__(self,root,json_data):
        #inicializamos root
        self.root = root
        #Ajustamos tamaños de las ventanas con las siguientes funciones
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        #lista vacia para guardar los datos
        cells =[]
        #recorrer json y añadir sus datos a las celdas de la lista vacía
        for animales in json_data:
            name = animales.get("name")
            descripcion = animales.get("description")
            image_url = animales.get("image_url")
            #guardar en una celda los datos del json
            cell = Cell(name,image_url,descripcion)
            #añadimos la celda a la lista 
            cells.append(cell)
        #recorremos la lista de celdas para que se muestran en la ventana principal
        for i, cell in enumerate (cells):
            label = ttk.Label(root,image=cell.Image_tk, text=cell.name,compound=tk.BOTTOM)
            label.grid(row=i,column=0)
            #con esto si clickamos en una imagen nos lleva a otra ventana con su nombre y descripcion y foto
            label.bind("<Button-1>", lambda event, cell = cell : detail_window(cell))
        #creamos la barra de menus 
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            #indicamos la etiqueta que sale en la ventana principal
                label="Acerca de ",
                #inddicamos que accion realiza al clicar en ayuda
                command=self.onButtonClicked
                )
        #añadimos a la barra menus
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
        root.config(menu=barra_menus)
        #cerramos el bucle
        root.mainloop()
            
        
 
    



    
            
        


        