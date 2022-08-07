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
        self.geometry('550x550')

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
        self.timeLabel = TimeLabel(self)
        self.imgDict = {1: self.img1, 2: self.img2, 3: self.img3, 4: self.img4, 5: self.img5, 6: self.img6, 7: self.img7, 8: self.img8, 9: self.img1Copy, 10: self.img2Copy, 11: self.img3Copy, 12: self.img4Copy, 13: self.img5Copy, 14: self.img6Copy, 15: self.img7Copy, 16: self.img8Copy}
        self.matchedTiles = 0
        self.objTargetList = list(self.imgDict.values())    
        self.dictList = list(self.imgDict.keys())
        #list stores obj name when button is pressed
        self.objList = []
        self.run()


    def layout(self):
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

        for row in range(0,4,1):
            for column in range(0,4,1):
                self.imgList[row*4+column].grid(row = row, column = column)

        self.quitButton.grid(row = 4, column = 0)
        self.timeLabel.grid(row =5, column = 0)

    def clickHandler(self, id):
        self.targetList.append(id)
        #what button user has pressed
        if id == 1:
            self.objList.append(self.img1)
            self.img1.flip()
            
        elif id == 2:
            self.objList.append(self.img2)
            self.img2.flip()

        elif id == 3:
            self.objList.append(self.img3)
            self.img3.flip()
        elif id == 4:
            self.objList.append(self.img4)
            self.img4.flip()
        elif id == 5:
            self.objList.append(self.img5)
            self.img5.flip()
        elif id == 6:
            self.objList.append(self.img6)
            self.img6.flip()
        elif id == 7:
            self.objList.append(self.img7)
            self.img7.flip()
        elif id == 8:
            self.objList.append(self.img8)
            self.img8.flip()
        elif id == 9:
            self.objList.append(self.img1Copy)
            self.img1Copy.flip()
        elif id == 10:
            self.objList.append(self.img2Copy)
            self.img2Copy.flip()
        elif id == 11:
            self.objList.append(self.img3Copy)
            self.img3Copy.flip()
        elif id == 12:
            self.objList.append(self.img4Copy)
            self.img4Copy.flip()
        elif id == 13:
            self.objList.append(self.img5Copy)
            self.img5Copy.flip()
        elif id == 14:
            self.objList.append(self.img6Copy)
            self.img6Copy.flip()
        elif id == 15:
            self.objList.append(self.img7Copy)
            self.img7Copy.flip()
        elif id == 16:
            self.objList.append(self.img8Copy)
            self.img8Copy.flip()

        if len(self.objList) == 2:
            # print('length of objList ==2')
            self.after(3000, self.compare())
       
    def compare(self):
        target1 = self.objList[0]
        target2 = self.objList[1]

        if target1.id == target2.id:
            messagebox.showinfo('showinfo', 'Pick 2 different tiles')
            self.matchedTiles -=1

        if target1.value() == target2.value():
            self.matchedTiles += 1
            if self.matchedTiles == 8:
                messagebox.showinfo('showinfo', 'You have matched all tiles')
                self.timeLabel.stop()

            self.objList.clear()
            self.targetList.clear()
        else:
            print('not a match...flipping targets')
            time.sleep(2)
            target1.flip()
            target2.flip()
            
            self.update()
            self.targetList.clear()
            self.objList.clear()

        self.debug()
        
    def run(self):
        self.layout()
        self.timeLabel.start()
                

    def debug(self):
        # print('self.numList ', self.numList)
        # print('targetList: ', self.targetList)
        print('objList: ', self.objList)
        print('matchedTiles ', self.matchedTiles)


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
        
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 1 is called')
                 

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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 2 is called')

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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)

        self.update()
        # print('flip function 3 is called')
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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 4 is called')
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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 5 is called')
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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 6 is called')
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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 7 is called')
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
        Button.__init__(self, image = self.active, command = lambda: self.g.clickHandler(self.id))
    def value(self):
        return self.n
    def flip(self):
        self.active, self.inactive = self.inactive, self.active
        self.config(image = self.active)
        self.update()
        # print('flip function 8 is called')

class QuitGame(Button):
    def __init__(self, master):
        self.g = master
        Button.__init__(self, text = 'Quit Game', command = self.quit, width = 10, height = 2, font = 'bold')

class TimeLabel(Label):
    def __init__(self,master):
        self.g = master
        self.run = False
        self.counter = -1
        self.sec = 0
        self.min = 0
        self.hours = 0
        Label.__init__(self, text = '00:00:00', font = ('Arial', 30))
    def start(self):
        print('timer is starting')
        self.run = True
        if self.run:
            self.update_time()
            self.run = True            
            self.counter += 1
        
    def stop(self):
        self.run = False
        self.update()

    def update_time(self):
        # print('timer is updating')
        if self.run:
            self.sec += 1 
        if self.sec ==60:
            self.min +=1
            self.sec = 0
        if self.min == 60:
            self.hours += 1
            self.min = 0
        
        hours_string = f'{self.hours}' if self.hours >9 else f'0{self.hours}'
        minutes_string = f'{self.min}' if self.min > 9 else f'0{self.min}'
        seconds_string = f'{self.sec}' if self.sec >9 else f'0{self.sec}'

        self.config(text = hours_string + ':' + minutes_string + ':' + seconds_string)
        self.after(1000, self.update_time)

if __name__ == '__main__':
    app = MemoryTile()
    app.mainloop()