from tkinter import Canvas, Frame, Label, Scrollbar, ttk
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
        self.root.resizable(True,True)
        #Ajustamos tamaños de las ventanas con las siguientes funciones
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        #lista vacia para guardar los datos
        self.cells =[]
        #recorrer json y añadir sus datos a las celdas de la lista vacía
        for animales in json_data:
            name = animales.get("name")
            descripcion = animales.get("description")
            image_url = animales.get("image_url")
            #guardar en una celda los datos del json
            cell = Cell(name,image_url,descripcion)
            #añadimos la celda a la lista 
            self.cells.append(cell)
        #scrollbar
        self.canvas = Canvas (self.root)
        self.scrollbar = Scrollbar (self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame= Frame(self.canvas)
        #usamos el método bind con Configure para indicar que cada vez que el Frame cambie de
        #tamaño se actualiza la región de desplazamiento del Canvas.
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        #indicamos posicion del frame dentro del canvas
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        #refactorizamos codigo para recorrer json 
        for i, cell in enumerate (self.cells):
            self.add_item(cell)
        #posiciones
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0,column=1, sticky="ns")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure (0, weight=1)        
        #creamos la barra de menus 
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            #indicamos la etiqueta que sale en la ventana principal
                label="Acerca de ",
                #inddicamos que accion realiza al clicar en ayuda
                #si meto los parentesis se lanza al momento y si no lo ponemos se lanza una clicamos
                command=self.onButtonClicked
                )
        #añadimos a la barra menus
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
        self.root.config(menu=barra_menus)
        #cerramos el bucle
        self.root.mainloop()


    def add_item(self, cell):
        frame = Frame (self.scrollable_frame)
        frame.pack(pady=10)

        label = Label (frame, image = cell.Image_tk, text= cell.name, compound= tk.BOTTOM)
        label.grid(row = 0, column=0)

        label.bind("<Button-1>", lambda event, cell=  cell : detail_window(cell))
    


        
            
        
 
    



    
            



  

