#set 5  
from tkinter import *
from tkinter import filedialog as fd
import wikipedia
root = Tk()
root.title('Custom Notebook App')

root.geometry('400x400')

# class Search:
#     def search_info(self, user_info):   
#         info = wikipedia.summary(user_info, sentences = 1)
#         return info

# class UI(Search):
#     def __init__(self):
#         self.s = search
#         self.search_label = Label(root, text = 'Search')
#         self.entryBox = Entry(root)
#         self.submit_bttn = Button(root, text = 'Submit', command = self.submit)
#         self.textbox = Text(root, width = 35, height = 20)
#     def grid(self):
#         self.search_label.grid(row = 0, column = 0)
#         self.entryBox.grid(row = 0, column = 1)
#         self.submit_bttn.grid(row = 0, column = 2)
#         self.textbox.grid(row = 1, column =1)
#     def submit(self):
#         self.textbox.delete('1.0', END)
#         user_info = self.entryBox.get()
#         # info = wikipedia.summary(user_info, sentences = 1)
#         # self.s.search_info(user_info)
       
#         self.textbox.insert(END, self.search_info(user_info))

# search = Search()

# app = UI()
# app.grid()


# root.mainloop()

class UI:
    def __init__(self):
        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.helpmenu = Menu(self.menubar, tearoff =0)
        self.text = Text(root)
    def commands(self):
        self.filemenu.add_command(label = 'New', command = self.new_func)
        self.filemenu.add_command(label = 'Open', command = self.open_func)
        self.filemenu.add_command(label = 'Save', command = self.save_func)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = 'Exit', command = self.exit_func)
        self.menubar.add_cascade(label = 'File', menu = self.filemenu)

        self.helpmenu.add_command(label = 'About', command = self.about_func)
        self.menubar.add_cascade(label = 'Help', menu = self.helpmenu)
        self.text.pack()


    def new_func(self):
        global file_name
        file_name = None
        self.text.delete('1.0', 'end')
    def open_func(self):
        pass
    def save_func(self):
        file_name = fd.asksaveasfilename()
        file_name.write(self.text)
        #run this and ask how to save file once 
        #contents are written to it
    def exit_func(self):
        pass
    def about_func(self):
        pass

app = UI()
app.commands()

root.config(menu = app.menubar)
root.mainloop()