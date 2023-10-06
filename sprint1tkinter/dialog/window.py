from tkinter import ttk,Button
from yes_window import show_yes_window
from no_window import show_no_window
class MainWindow():
    #definimos 2 funciones a las cuales le pasamos el metodo de cada clase de la 
    #ventana que queramos que se ejecute; con esto cuando clicamos le enviamos uno o el otro y realizara la acción
    def on_button_clicked_yes(self):
        show_yes_window()
    def on_button_clicked_no(self):
        show_no_window()
    #self es igual a this en java
    #es un constructor esto
    def __init__(self,root):
        #inicializamos root
        self.root = root
        #frame sirve para empaquetar widgets como etiquetas,botones ...
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        ##añadimos etiqueta
        self.label = ttk.Label(self.frame,text = "¿Deseas algo?")
        self.label.pack()
        #añadimos un botón y hay que decirle quien es el padre
        #añadimos un texto y con command decimos que hace al presionar
        self.button = ttk.Button(self.frame,text="sí",command=self.on_button_clicked_yes)
        self.button.pack(side="left",expand=True)
        #otro boton identico al anterior pero con otra funcion y acción a realizar
        self.button1 = ttk.Button(self.frame,text="no",command=self.on_button_clicked_no)
        self.button1.pack(side="right",expand=True)

        