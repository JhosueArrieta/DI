from tkinter import ttk,Button

class MainWindow():
    #este boton no hace nada pq tiene pass
    def on_button_clicked(self):
        pass
    #self es igual a this en java
    #es un constructor esto
    def __init__(self,root):
        #inicializamos root
        self.root = root
        #frame sirve para empaquetar widgets como etiquetas,botones ...
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        ##añadimos etiqueta
        self.label = ttk.Label(self.frame,text = "Este mensaje es poco importante")
        self.label.pack()
        #añadimos un botón y hay que decirle quien es el padre
        #añadimos un texto y con command decimos que hace al presionar
        self.button = ttk.Button(self.frame,text="realizar acción",command=self.on_button_clicked)
        self.button.pack()