from PIL import ImageTk,Image

class Cell :
    def __init__(self,title,path,desc):
        self.title = title
        self.path = path
        #img = Image.open(self.path)
        #img1 = img.resize(100,100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(file=self.path)
        self.desc = desc
        
    