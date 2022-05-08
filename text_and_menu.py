#set 5  
from tkinter import *
import wikipedia
root = Tk()
root.title('Information from wikipedia')

root.geometry('400x400')

class Search:
    def search_info(self, user_info):   
        info = wikipedia.summary(user_info, sentences = 1)
        return info

class UI(Search):
    def __init__(self):
        self.s = search
        self.search_label = Label(root, text = 'Search')
        self.entryBox = Entry(root)
        self.submit_bttn = Button(root, text = 'Submit', command = self.submit)
        self.textbox = Text(root, width = 35, height = 20)
    def grid(self):
        self.search_label.grid(row = 0, column = 0)
        self.entryBox.grid(row = 0, column = 1)
        self.submit_bttn.grid(row = 0, column = 2)
        self.textbox.grid(row = 1, column =1)
    def submit(self):
        self.textbox.delete('1.0', END)
        user_info = self.entryBox.get()
        # info = wikipedia.summary(user_info, sentences = 1)
        # self.s.search_info(user_info)
       
        self.textbox.insert(END, self.search_info(user_info))

search = Search()

app = UI()
app.grid()


root.mainloop()
