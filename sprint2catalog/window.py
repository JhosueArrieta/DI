from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import detail_window
from PIL import Image, ImageTk

class MainWindow():
    def onButtonClicked(self, cell):
       detail_window(cell)

    def __init__(self,root,json_data):
        #inicializamos root
        self.root = root
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
            label.bind("<Button-1>", lambda event, cell = cell : self.onButtonClicked(cell))
            
        
 
    



    
            
        


        