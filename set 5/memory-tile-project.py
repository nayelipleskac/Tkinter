#set 7  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd
from PIL import Image, ImageTk
import random, time

# root = Tk()

class MemoryTile(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Memory Tile Project')
        self.geometry('500x500')

        self.numList = []
        self.imgList = []
        self.targetList = []

        self.img1 = Img1(self, 1)
        self.img1Copy = Img1(self, 9)
        self.img2 = Img2(self,2)
        self.img2Copy = Img2(self, 10)
        self.img3 = Img3(self,3)
        self.img3Copy = Img3(self, 11)
        self.img4 = Img4(self, 4)
        self.img4Copy = Img4(self, 12)
        self.img5 = Img5(self, 5)
        self.img5Copy = Img5(self, 13)
        self.img6 = Img6(self, 6)
        self.img6Copy = Img6(self, 14)
        self.img7 = Img7(self, 7)
        self.img7Copy = Img7(self, 15)
        self.img8 = Img8(self, 8)
        self.img8Copy = Img8(self, 16)
        self.quitButton = QuitGame(self)
        # self.timeLabel = TimeLabel(self)
        self.imgDict = {1: self.img1, 2: self.img2, 3: self.img3, 4: self.img4, 5: self.img5, 6: self.img6, 7: self.img7, 8: self.img8, 9: self.img1Copy, 10: self.img2Copy, 11: self.img3Copy, 12: self.img4Copy, 13: self.img5Copy, 14: self.img6Copy, 15: self.img7Copy, 16: self.img8Copy}
        self.matchedTiles = 0
        self.objTargetList = list(self.imgDict.values())    
        self.dictList = list(self.imgDict.keys())
        #list stores obj name when button is pressed
        self.objList = []


    def grid(self):
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
        random.shuffle(self.imgList)

        # for key, val in enumerate(self.imgList):
        #     self.imgDict[key] = val

        for row in range(0,4,1):
            for column in range(0,4,1):
                self.imgList[row*4+column].grid(row = row, column = column)

        self.quitButton.grid(row = 4, column = 0)

    def clickHandler(self, target, val, pokemon_img, questionmark, id):
        self.targetList.append(id)
        #what button user has pressed
        if id == 1:
            self.objList.append(self.img1)
            # self.img1.config(image = pokemon_img)
            print('img has been flipped')
            self.img1.flip()
        elif id == 2:
            self.objList.append(self.img2)
            self.img2.config(image = pokemon_img) 
        elif id == 3:
            self.objList.append(self.img3)
            self.img3.config(image = pokemon_img)
        elif id == 4:
            self.objList.append(self.img4)
            self.img4.config(image = pokemon_img)
        elif id == 5:
            self.objList.append(self.img5)
            self.img5.config(image = pokemon_img)
        elif id == 6:
            self.objList.append(self.img6)
            self.img6.config(image = pokemon_img)
        elif id == 7:
            self.objList.append(self.img7)
            self.img7.config(image = pokemon_img)
        elif id == 8:
            self.objList.append(self.img8)
            self.img8.config(image = pokemon_img)
        elif id == 9:
            self.objList.append(self.img1Copy)
            self.img1Copy.config(image = pokemon_img)
        elif id == 10:
            self.objList.append(self.img2Copy)
            self.img2Copy.config(image = pokemon_img)
        elif id == 11:
            self.objList.append(self.img3Copy)
            self.img3Copy.config(image = pokemon_img)
        elif id == 12:
            self.objList.append(self.img4Copy)
            self.img4Copy.config(image = pokemon_img)
        elif id == 13:
            self.objList.append(self.img5Copy)
            self.img5Copy.config(image = pokemon_img)
        elif id == 14:
            self.objList.append(self.img6Copy)
            self.img6Copy.config(image = pokemon_img)
        elif id == 15:
            self.objList.append(self.img7Copy)
            self.img7Copy.config(image = pokemon_img)
        elif id == 16:
            self.objList.append(self.img8Copy)
            self.img8Copy.config(image = pokemon_img)
        # time.sleep(1)

        if len(self.targetList) == 2 and len(self.objList) == 2:
            self.after(3000, self.compare(questionmark))
            # target1 = self.targetList[0]
            # target2 = self.targetList[1]
            # if self.imgDict[target1].value() == self.imgDict[target2].value():
            #     print('MATCH')
            #     self.matchedTiles += 1
            #     if self.matchedTiles == 8:
            #         messagebox.showinfo('showinfo', 'You have matched all tiles')
            #     self.debug()
            #     self.targetList.clear()
                
            # else: 
            #     #change img type to question mark
            #     print('NOT A MATCH')
            #     # self.after(2000, compare)
            #     # time.sleep(3)
            #     self.debug()
            #     self.objList[0].config(image = questionmark)
            #     self.objList[1].config(image = questionmark)
                
            #     self.update()
            #     self.targetList.clear()
            #     self.objList.clear()
    def compare(self, questionmark):
        # target1 = self.targetList[0]
        # target2 = self.targetList[1]
        target1 = self.objList[0]
        target2 = self.objList[1]

        # if self.imgDict[target1].value() == self.imgDict[target2].value():
        if target1.value() == target2.value():

            print('MATCH')
            self.matchedTiles += 1
            if self.matchedTiles == 8:
                messagebox.showinfo('showinfo', 'You have matched all tiles')
            self.debug()
            self.targetList.clear()
        else:
            self.after(3000,self.notAMatch(target1, target2, questionmark))
            
    def notAMatch(self, target1, target2, questionmark):
        target1.config(image = questionmark)
        target2.config(image = questionmark)
        print('NOT A MATCH')
        self.update()
        self.targetList.clear()
        self.objList.clear()


        # for x in range(1,17,1):
        #     if id==x: 
        #         self.imgDict[id].config(image = pokemon_img)

        
    def run(self):
        pass
        #in __init__ self.run() 
        # self.timeLabel.start()
                

    def debug(self):
        print('self.numList ', self.numList)
        print('targetList: ', self.targetList)
        print('objList: ', self.objList)
        # print('what class obj number user pressed ',self.imgDict[target])
        # index = self.imgList.index()

#create a flip function for every class

class Img1(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(1,'Img1', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        # self.btn.config(image = self.inactive)
        self.update()
        #change image val 
        #call flip() if two tiles are not matched 
        

class Img2(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(2,'Img2', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
class Img3(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(3,'Img3', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
class Img4(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(4,'Img4', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
class Img5(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(5,'Img5', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
class Img6(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(6,'Img6', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
class Img7(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(7,'Img7', self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n
class Img8(Button):
    def __init__(self, master, id):
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
        self.id = id
        self.active = self.final_question_img
        self.inactive = self.final_pokemon_img
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(8,'Img8',self.final_pokemon_img, self.final_question_img, self.id))
    def value(self):
        return self.n

class QuitGame(Button):
    def __init__(self, master):
        self.g = master
        Button.__init__(self, text = 'Quit Game', command = self.quit, width = 10, height = 2, font = 'bold')
    def quit(self):
        print('in self.quit')
        self.quit()

# class TimeLabel(Label):
#     def __init__(self,master, time, sec):
#         self.g = master
#         self.time = time
#         self.sec = 0
#         self.min = sec //60
#         self.hour = min // 60
#         Label.__init__(self, text = 'Time Taken: {}'.format(self.hour))
#     def start(self):
#         start_time = time.time()
#         while True:
#             self.sec += 1
#             if self.sec == 59:
#                 self.min += 1



# while True:


if __name__ == '__main__':
    app = MemoryTile()
    app.grid()
    # app.run()
    app.mainloop()
    # app.matchImg()
    # app.mainloop()
