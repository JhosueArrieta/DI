from tkinter import ttk
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk
from detail_window import detail_window
#######################
import requests
from PIL import Image , ImageTk
from io import BytesIO
import json
import threading
class MainWindow():
     #def onButtonClicked(self, cell):
     #  detail_window(cell)
    def __init__(self,root,json_data):
        #inicializamos root
        self.root = root
        #lista vacia para guardar los datos
        self.cells =[]
        #convertir json a lista de diccionarios
      #lista_datos = json.loads(json_data)
        #recorrer json y añadir sus datos a las celdas de la lista vacía
        for animales in json_data:
            name = animales.get("name")
            descripcion = animales.get("description")
            image_url = animales.get("image_url")
            self.thread = threading.Thread(target=self.load_image_from_url)
            self.thread.start()

            animal_data = {
                "name": name,
                "description": descripcion,
                "image_url": image_url
            }

            self.cells.append(animal_data)
        
        for animal in self.cells:
            name = animal.get("name")
            description = animal.get("description")
            image_url = animal.get("image_url")

    def load_image_from_url (self,url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
    



    
            
        


        