import threading
import tkinter as tk
class loading:
    #iniciamos constructor
    def __init__(self,root):
        self.root = root
        #titulo de la ventana
        self.root.title("Cargando...")
        #dimensiones de la ventana
        self.root.geometry("170x120")
        #con esto no dejamos cambiar el tamaño de la ventana
        self.root.resizable(False,False)
        #creamos una etiqueta con el tipo y tamaño del texto a mostrar
        self.label = tk.Label(self.root, text="Cargando datos...",font=("Arial",14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")
        #representamos con una circunferencia el proceso de carga, pasamos el alto ancho y color    
        self.canvas = tk.Canvas(self.root,width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0
        #dibuja el circulo
        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        #self.thread = threading.Thread(target=self.fetch_json_data)
        #self.thread.start()

    def draw_progress_circle(self, progress):
        #eimina el objeto dibujado que tiene la tag asociada
        self.canvas.delete("progress")
        #le da el angulo a la circunferencia
        angle = int(360 * (progress / 100))
        #metodo encarargar de dibujar la circun
        self.canvas.create_arc(10, 10, 35, 35,
                            start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
    #metodo encargado de controlar el tiempo de vueltas de la circunferencia del proceso de carga
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 14.20
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)

              


