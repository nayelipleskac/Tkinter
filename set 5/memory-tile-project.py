#set 7  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd
from PIL import Image, ImageTk

root = Tk()
root.title('Memory Tile Project')

root.geometry('500x500')

class MemoryTile(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.numList = []
        self.imgList = []
        # self.imgTuple = ()
        self.img1 = Img1(self)
        self.img1Copy = Img1(self)
        self.img2 = Img2(self)
        self.img2Copy = Img2(self)
    def grid(self):
        self.img1.grid(row = 0, column = 0)
        self.img2.grid(row = 0, column = 1)
        self.img1Copy.grid(row = 0, column = 2)
        self.img2Copy.grid(row = 0, column = 3)
        #img 8, copy imgs x2
    def insertValue(self, target):
        self.t = None
        if target == 'Img1':
            print('img1 was pressed')
        if target == 'Img2':
            print('img2 was pressed')
    def matchImg(self):
        #use the hash mehtod 
        for i in range(1,9,1):
            self.numList.append(i)
            self.numList.append(i)


    def debug(self):
        print('self.numList ', self.numList)


class Img1(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/bulbasaur.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img1'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img1'))
    def value(self):
        return self.n
    def appendImgTuple(self):
        self.g.imgTuple.append(self.final_pokemon_img)

class Img2(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/bulbasaur.jpg')
        self.resize_img = self.question_mark_img.resize((100,100))
        self.final_img = ImageTk.PhotoImage(self.resize_img)
        self.n = 'Img2'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_img, command = lambda: self.g.insertValue('Img2'))
    def value(self):
        return self.n





if __name__ == '__main__':
    app = MemoryTile()
    app.grid()
    root.mainloop()
