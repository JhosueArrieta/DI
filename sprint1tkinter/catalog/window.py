from tkinter import ttk
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk
class MainWindow():
   
    def __init__(self,root):
        #inicializamos root
        self.root = root
        #añadimos un título
        self.root.title("Ejercicio Nº 5")
        #creamos una lista de celdas con las imágenes
        self.cells = [
            Cell("León","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\león.jpg"),
            Cell("Tigre","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\tigre_de_bengala.jpg"),
            Cell("Puma_negro","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\puma_negro.jpg"),
            Cell("Oso_pardo","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\oso_pardo.jpg"),
            Cell("Águila_real","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\águila_real.jpg")
        ]

        #recorremos la lista y printeamos cada imagen en funcion del label.grid
        #abrimos la imagen que recorre y la guardamos en una variable, luego redimensionamos dicha imagen y la guardamos
        #
        for i, cell in enumerate (self.cells):
            img = Image.open(cell.path)
            img1 = img.resize((100,100),Image.LANCZOS)
            #creamos un objeto ImageTk.PhotoImage a partir de la imagen redimensionada.
            cell.image_tk = ImageTk.PhotoImage(img1)
            #creamos la etiqueta que muestra la imagen en la parte inferior de dicha estiqueta y el titulo del elemento actual
            label = ttk.Label(root,image=cell.image_tk, text=cell.title,compound=tk.BOTTOM)
            #dicha etiqueta se coloca en la fila i y columna 0
            label.grid(row=i,column=0)
    
            
        


        