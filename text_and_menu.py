#set 5  
from tkinter import *
from tkinter import messagebox

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

# class File():
#     def __init__(self):
#         self.file_name = None
# class UI:
#     def __init__(self):
#         self.f = file
#         self.menubar = Menu(root)
#         self.filemenu = Menu(self.menubar, tearoff = 0)
#         self.helpmenu = Menu(self.menubar, tearoff =0)
#         self.options = Menu(self.menubar, tearoff = 0)
#         self.text = Text(root)
#     def commands(self):
#         self.filemenu.add_command(label = 'New', command = self.new_func)
#         self.filemenu.add_command(label = 'Open', command = self.open_func)
#         self.filemenu.add_command(label = 'Save', command = self.save_func)
#         self.filemenu.add_separator()
#         self.filemenu.add_command(label = 'Exit', command = self.exit_func)
#         self.menubar.add_cascade(label = 'File', menu = self.filemenu)
#         self.helpmenu.add_command(label = 'About', command = self.about_func)
#         self.menubar.add_cascade(label = 'Help', menu = self.helpmenu)
#         self.text.pack()
#         self.options.add_command(label = 'Configure Notepad', command = self.configure)
#         self.menubar.add_cascade(label = 'Options', menu = self.options)


#     def new_func(self):
#         self.text.delete('1.0', 'end')
#     def open_func(self):

#         self.f.file_name = fd.askopenfilename()
#         f = open(self.f.file_name, 'r')
        
#         #file to textbox
#         with open(self.f.file_name) as f: 
#             lines = f.readlines()
#         self.text.insert('1.0', lines)
#         f.close()
#     def save_func(self):   
        
#         #edit file
#         if self.f.file_name != '':
#             f = open(self.f.file_name, 'w')
#             text_contents = self.text.get('1.0', 'end-1c')
#             print(text_contents)
#             f.write(str(text_contents))
#         else:
#             self.f.file_name = fd.asksaveasfilename()    
#             f = open(self.f.file_name + '.txt', 'w')
#             text_contents = self.text.get('1.0', 'end-1c')
#             print(text_contents)

#             f.write(str(text_contents))

        
        
        
#     def exit_func(self):
#         root.destroy()
#     def about_func(self):
#         messagebox.showinfo('showinfo', 'This notepad application allowsthe user to create new files and save them, or edit existing files.')
#     def configure(self):
#         self.text.configure(font= ('Times New Roman', 10, 'italic'), fg = 'red', bg = 'black')

# file = File()

# app = UI()
# app.commands()

# root.config(menu = app.menubar)
# root.mainloop()

#Options Menu set 5

class Register():
    def __init__(self):
        self.dayVar = StringVar()
        self.monthVar = StringVar()
        self.yearVar = StringVar()
        self.months= ['1', '2', '3', '4', '5']
        self.days= ['1', '2', '3', '4', '5', '6']
        self.years = ['2001', '2002', '2003', '2004', '2005']
    def generateOptions(self):
        for days in range(1,32,1):
            self.days.append(days)
        for months in range(1,13,1):
            self.months.append(months)
        for years in range(2000, 2023, 1):
            self.years.append(years)
        print('days: ', days)
        print('months: ', months)
        print('years: ', years)


class UI:
    def __init__(self):
        self.r = register
        self.name_label = Label(root, text = 'Name')
        self.name_entry = Entry(root)

        self.DOB = Label(root, text = 'DOB')
        self.monthDayYear = Label(root, text = 'Month   Day    Year')
        self.month_dropdown = OptionMenu(root, self.r.monthVar, self.r.months)
        self.day_dropdown = OptionMenu(root, self.r.dayVar, self.r.days)
        self.year_dropdown = OptionMenu(root, self.r.yearVar, self.r.years)

        self.email = Label(root, text = 'Email')

        self.password = Label(root, text = 'Password')

        self.confirmPassword = Label(root, text = 'Confirm Password')
        
    def grid(self):
        self.name_label.grid(row= 0, column = 0)
        self.name_entry.grid(row = 0, column = 1)
        self.DOB.grid(row = 2, column = 0)
        self.monthDayYear.grid(row = 1, column = 1)
        self.month_dropdown.grid(row = 2, column = 1)
        self.day_dropdown.grid(row = 2, column = 2)
        self.year_dropdown.grid(row = 2, column = 3)
        self.email.grid(row = 3, column = 0)
        self.password.grid(row = 4, column = 0)
        self.confirmPassword.grid(row = 5, column = 0)



register =  Register()
# register.generateOptions()
app = UI()
app.grid()

root.mainloop()


