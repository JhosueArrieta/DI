from PIL import ImageTk,Image
import requests
from io import BytesIO
#iniciamos constructor para inicializar los atributos a usar 
class Cell :
    def __init__(self,name,url,desc): 
        self.name = name 
        self.url = url
        #con esto descargamos la imagen y la guardamos en Image_Tk
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        self.Image_tk = ImageTk.PhotoImage(img_data)
        self.desc = desc
    
   

        
        
    