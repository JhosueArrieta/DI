from tkinter import ttk,Button
import tkinter as tk
from cell import Cell

class MainWindow():
   
    def __init__(self,root):
        #inicializamos root
        self.root = root
        #añadimos un título
        self.root.title("Ejercicio Nº 5")
        #creamos una lista de celdas con las imágenes
        self.cells = [
            Cell("León","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\edited\\león.jpg"),
            Cell("Tigre","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\edited\\tigre_de_bengala.jpg"),
            Cell("Puma_negro","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\edited\\puma_negro.jpg"),
            Cell("Oso_pardo","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\edited\\oso_pardo.jpg"),
            Cell("Águila_real","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\edited\\águila_real.jpg")
        ]
        #recorremos la lista y printeamos cada imagen en funcion del label.grid
        for i, cell in enumerate (self.cells):
            label = ttk.Label(root,image=cell.image_tk, text=cell.title,compound=tk.BOTTOM)
            label.grid(row=i,column=0)
        


        