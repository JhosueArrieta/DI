from PIL import ImageTk,Image
#iniciamos constructor para inicializar los atributos a usar 
class Cell :
    def __init__(self,title,path,desc): 
        self.title = title
        self.path = path
        self.image_tk = ImageTk.PhotoImage(file=self.path)
        self.desc = desc
        
    