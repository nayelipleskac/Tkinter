#set 5  
from tkinter import *
import wikipedia
root = Tk()
root.title('Information from wikipedia')

root.geometry('300x400')

class Search:
    def __init__(self):
        self.a = app
    def search_info(self, user_info):
        info = wikipedia.summary(user_info, sentences = 1)
        self.a.textbox.insert(END, info)


class UI:
    def __init__(self):
        self.s = search
        self.search_label = Label(root, text = 'Search')
        self.entryBox = Entry(root)
        self.submit_bttn = Button(root, text = 'Submit', command = self.submit)
        self.textbox = Text(root)
    def grid(self):
        self.search_label.grid(row = 0, column = 0)
        self.entryBox.grid(row = 0, column = 1)
        self.submit_bttn.grid(row = 0, column = 2)
        self.textbox.grid(row = 1, column =1)
    def submit(self):
        self.textbox.delete('1.0', END)
        user_info = self.entryBox.get()
        self.s.search_info(user_info)

    


app = UI()
app.grid()
search = Search()

root.mainloop()
