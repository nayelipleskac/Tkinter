import webbrowser
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Jumbled words Game')
class Game:
    def __init__(self):
        self.words = ['Hello', 'Goodbye']
        self.c = None
        self.r = None

    def start(self):
        self.c = random.choice(self.words)
        self.r = list(self.c)
        random.shuffle(self.r)
        self.r = "".join(self.r)
        return self.r

    def compare(self,c):
        print('actual:{}\ninput:{}'.format(self.c,c))
        if self.c == c:
            messagebox.showinfo('showinfo','Correct!')
            return True

class UI:
    def __init__(self, root, game):
        self.r = root
        self.g = game
        self.w = None
        self.l1 = Label(root)
        self.b1 = Button(root,text='CLICK TO GENERATE', command = lambda: self.start())
        self.b2 = Button(root,text='Submit', command = self.submit)
        self.e1 = Entry()
        self.pack()
    def start(self):
        self.w = self.g.start()
        self.l1.config(text=self.w)
        self.r.update()
    def submit(self):
        if self.g.compare(self.e1.get()):
            messagebox.showinfo('showinfo','Correct!')
        else:
            messagebox.askretrycancel('Retry?', 'Do you want to try again?')

    def pack(self):
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0,column=1)
        self.e1.grid(row=2,column=1)
        self.l1.grid(row=2,column=0)
game = Game()
app = UI(root, game)
root.mainloop()