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
        #use dictionary instead of tuple
        # self.imgTuple = ()
        self.img1 = Img1(self)
        self.img1Copy = Img1(self)
        self.img2 = Img2(self)
        self.img2Copy = Img2(self)
        self.img3 = Img3(self)
        self.img3Copy = Img3(self)
        self.img4 = Img4(self)
        self.img4Copy = Img4(self)
        self.img5 = Img5(self)
        self.img5Copy = Img5(self)
        self.img6 = Img6(self)
        self.img6Copy = Img6(self)
        self.img7 = Img7(self)
        self.img7Copy = Img7(self)
        self.img8 = Img8(self)
        self.img8Copy = Img8(self)
    
    def grid(self):
        self.img1.grid(row = 0, column = 0)
        self.img1Copy.grid(row = 0, column = 2)
        self.img2.grid(row = 0, column = 1)
        self.img2Copy.grid(row = 0, column = 3)
        self.img3.grid(row = 1, column = 0)
        self.img3Copy.grid(row = 1, column = 1)
        self.img4.grid(row = 1, column = 2)
        self.img4Copy.grid(row = 1, column = 3)
        self.img5.grid(row= 2, column =0)
        self.img5Copy.grid(row = 2, column = 1)
        self.img6.grid(row = 2, column = 2)
        self.img6Copy.grid(row = 2,column = 3)
        self.img7.grid(row = 3, column = 0)
        self.img7Copy.grid(row = 3, column = 1)
        self.img8.grid(row= 3,column = 2)
        self.img8Copy.grid(row = 3, column = 3)

        #img 8, copy imgs x2
    def insertValue(self, target):
        self.t = None
        if target == 'Img1':
            print('img1 was pressed')
        if target == 'Img2':
            print('img2 was pressed')
        if target == 'Img3':
            print('img3 was pressed')
        if target == 'Img4':
            print('img4 was pressed')
        if target == 'Img5':
            print('img5 was pressed')
        if target == 'Img6':
            print('img6 was pressed')
        if target == 'Img7':
            print('img7 was pressed')
        if target == 'Img8':
            print('img8 was pressed')
        self.debug()
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
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/eevee.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img2'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img2'))
    def value(self):
        return self.n
class Img3(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/rayquaza.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img3'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img3'))
    def value(self):
        return self.n
class Img4(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/snorlax.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img4'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img4'))
    def value(self):
        return self.n
class Img5(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/pikachu.png')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img5'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img5'))
    def value(self):
        return self.n
class Img6(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/gyarados.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img6'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img6'))
    def value(self):
        return self.n
class Img7(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/torchic.png')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img7'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img7'))
    def value(self):
        return self.n
class Img8(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/vaporeon.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'Img8'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_pokemon_img, command = lambda: self.g.insertValue('Img8'))
    def value(self):
        return self.n



if __name__ == '__main__':
    app = MemoryTile()
    app.grid()
    app.matchImg()
    root.mainloop()
