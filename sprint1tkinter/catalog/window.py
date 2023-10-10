from tkinter import ttk
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk
from detail_window import detail_window
class MainWindow():
     def onButtonClicked(self, cell):
        detail_window(cell)
     def __init__(self,root):
        #inicializamos root
        self.root = root
        #añadimos un título
        self.root.title("Ejercicio Nº 7")
        #creamos una lista de celdas con las imágenes
        self.cells = [
            Cell("León","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\león.jpg","El león es un majestuoso felino conocido por su melena y su poderío. Es el rey de la selva y simboliza fuerza y liderazgo. "),
            Cell("Tigre","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\tigre_de_bengala.jpg","El tigre de Bengala es un felino impresionante y poderoso, con rayas distintivas y una presencia imponente."),
            Cell("Puma_negro","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\puma_negro.jpg","El puma negro, también conocido como pantera negra, es un felino de gran elegancia y misterio. Su pelaje oscuro y su mirada penetrante lo hacen un verdadero enigma de la naturaleza. "),
            Cell("Oso_pardo","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\oso_pardo.jpg","El oso pardo es un imponente mamífero que habita en diversos ecosistemas. Con su pelaje grueso y su poderosa presencia, es un símbolo de fuerza y resistencia en la naturaleza."),
            Cell("Águila_real","C:\\msys64\\home\\arrie\\DI\\sprint1tkinter\\catalog\\data\\unedited\\águila_real.jpg","El águila real es un majestuoso ave rapaz, con una envergadura impresionante y una mirada aguda. Su vuelo elegante y su poderoso pico la convierten en un símbolo de libertad y grandeza.")
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
            label.bind("<Button-1>", lambda event, cell = cell : self.onButtonClicked(cell))
    
            
        


        