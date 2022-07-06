#set 7  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd
from PIL import Image, ImageTk
import random

root = Tk()
root.title('Memory Tile Project')

root.geometry('500x500')

class MemoryTile(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.numList = []
        self.imgList = []
        self.targetList = []
        #use dictionary instead of tuple
        #coment
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
        self.imgDict = {1: self.img1, 2: self.img2, 3: self.img3, 4: self.img4, 5: self.img5, 6: self.img6, 7: self.img7, 8: self.img8, 9: self.img1Copy, 10: self.img2Copy, 11: self.img3Copy, 12: self.img4Copy, 13: self.img5Copy, 14: self.img6Copy, 15: self.img7Copy, 16: self.img8Copy}
        self.objTargetList = list(self.imgDict.values())    
    def grid(self):
        # append self.imgn in self.imgList; shuffle list; 
        self.imgList.append(self.img1)
        self.imgList.append(self.img2)
        self.imgList.append(self.img3)
        self.imgList.append(self.img4)
        self.imgList.append(self.img5)
        self.imgList.append(self.img6)
        self.imgList.append(self.img7)
        self.imgList.append(self.img8)
        self.imgList.append(self.img1Copy)
        self.imgList.append(self.img2Copy)
        self.imgList.append(self.img3Copy)
        self.imgList.append(self.img4Copy)
        self.imgList.append(self.img5Copy)
        self.imgList.append(self.img6Copy)
        self.imgList.append(self.img7Copy)
        self.imgList.append(self.img8Copy)

        for x in range(0,2,1):
            for y in range(0,8,1):
                self.numList.append(y)

        random.shuffle(self.numList)
        #mapping the list
        # for index, value in enumerate(self.numList):
        #     self.imgDict[index] = value

        random.shuffle(self.imgList)

        for key, val in enumerate(self.imgList):
            self.imgDict[key] = val
        #result: {0: img3, 1: img4, ...}
        # for x in self.imgList:
        #     self.imgDict[x] = img

        for row in range(0,4,1):
            for column in range(0,4,1):
                self.imgList[row*4+column].grid(row = row, column = column)
                # self.imgDict[

    def insertValue(self, target, val, pokemon_img, questionmark):
        self.t = None
        # print(target)
        # self.dictList = list(self.imgDict.keys())
        # print('list of dict keys', self.dictList)
        # self.imgDict[key] = 
        self.targetList.append(target)
        
        if len(self.targetList) == 2:
            target1 = self.targetList[0]
            target2 = self.targetList[1]
            print('imgDict[target1].value()', self.imgDict[target1].value())
            print('imgDict[target2].value()', self.imgDict[target2].value())
            if self.imgDict[target1].value() == self.imgDict[target2].value():
        #     if self.targetList[0] == self.targetList[1]:
                print('MATCH')
                self.debug()
                self.targetList.clear()
            #change img type to pokemon img
            # self.targetList[0].config(image = pokemon_img)
            else: 
                print('NOT A MATCH')
                print('targetlist[0]', self.targetList[0])
                print('targetList[1]', self.targetList[1])
                self.debug()
                self.targetList.clear()
            #change img type to question mark
            #comparing class objects instead of strings 
            # self.targetList[0].config(image = questionmark)
            # self.targetList[1].config(image = questionmark)
        
        if val == 'Img1':
            print('img1 was pressed')  
            #change img type to pokemon img 
            self.img1.config(image = pokemon_img)
        if val == 'Img2':
            print('img2 was pressed')
            self.img2.config(image = pokemon_img)

        if val == 'Img3':
            print('img3 was pressed')
            self.imgDict[target].value().config(image = pokemon_img)
        if val == 'Img4':
            print('img4 was pressed')
            self.img4.config(image = pokemon_img)
        if val == 'Img5':
            print('img5 was pressed')
            self.img5.config(image = pokemon_img)
        if val == 'Img6':
            print('img6 was pressed')
            self.img6.config(image = pokemon_img)
        if val == 'Img7':
            print('img7 was pressed')
            self.img7.config(image = pokemon_img)
        if val == 'Img8':
            print('img8 was pressed')
            self.img8.config(image = pokemon_img)
        if val == self.imgList[0]:
            print('img')
    def matchImg(self):
        pass
        #use the hash method 
        # {1: Img1, 2: Img2, 3: Img3, 4: Img4}
        # for x in range(1, 3, 1):
        #     for i in range(1,9,1):
        #         self.numList.append(i)
#match ids to imgs; if the two ids match, the imgs are the same

    def debug(self):
        print('self.numList ', self.numList)
        print('targetList: ', self.targetList)
        # index = self.imgList.index()

class Img1(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/bulbasaur.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'bulbasaur'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(1,'Img1', self.final_pokemon_img, self.final_question_img))
    def value(self):
        return self.n

class Img2(Button):
    def __init__(self, master):
        self.g = master
        self.question_mark_img = Image.open(r'C:/Users/plesk/Downloads/question-mark.png') 
        self.pokemon_img = Image.open(r'C:/Users/plesk/Downloads/eevee.jpg')
        self.resize_question_img = self.question_mark_img.resize((100,100))
        self.resize_pokemon_img = self.pokemon_img.resize((100,100))
        self.final_question_img = ImageTk.PhotoImage(self.resize_question_img)
        self.final_pokemon_img = ImageTk.PhotoImage(self.resize_pokemon_img)
        self.n = 'eevee'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(2,'Img2', self.final_pokemon_img, self.final_question_img))
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
        self.n = 'rayquaza'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(3,'Img3', self.final_pokemon_img, self.final_question_img))
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
        self.n = 'snorlax'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(4,'Img4', self.final_pokemon_img, self.final_question_img))
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
        self.n = 'pikachu'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(5,'Img5', self.final_pokemon_img, self.final_question_img))
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
        self.n = 'gyarados'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(6,'Img6', self.final_pokemon_img, self.final_question_img))
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
        self.n = 'torchic'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(7,'Img7', self.final_pokemon_img, self.final_question_img))
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
        self.n = 'vaporeon'
        self.button_state = 'NORMAL'
        self.row_val = 0
        self.column_val = 0
        self.is_clicked = 0
        Button.__init__(self, image = self.final_question_img, command = lambda: self.g.insertValue(8,'Img8',self.final_pokemon_img, self.final_question_img))
    def value(self):
        return self.n



if __name__ == '__main__':
    app = MemoryTile()
    app.grid()
    app.matchImg()
    root.mainloop()
