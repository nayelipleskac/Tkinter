#set 4
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pytz, random
from datetime import datetime
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

# excsise 1
# colors = ['red', 'green', 'blue', 'purple', 'orange']

# title = Label(root, text = 'COLORS')
# title.grid(row = 0, column = 0)

# color_label = Label(root, bg = 'white', width = 8)
# color_label.grid(row = 2, column = 0)

# #creating a Listbox
# listbox_1 = Listbox(root)
# listbox_1.grid(row = 1, column = 0)


# #append a value to the Listbox
# for i in colors:
#     listbox_1.insert(END, i)

# def change_color():
#     print('get_index')
#     selection = listbox_1.curselection()
#     for item in selection:
#         print('you have selected index ' + str(item))
#         index = str(item)
#         actual_value = listbox_1.get(index)
#         #change color_label bg
#         color_label.configure(bg = actual_value)
#         print(actual_value, ' :actual value')
#         # print('selection index ', selection[item])

# button = Button(root, text = 'submit', command= change_color)
# button.grid(row = 3, column = 1)
# root.mainloop()

#exercise 2

# class Timezone:
#     def __init__(self):
#         # self.i = index
#         self.timezones = pytz.all_timezones #all timezones
    
#     def display_timezone(self):
#         pass 


# class UI:
#     def __init__(self):
#         self.t = timezoneApp
#         self.title = Label(root, text = 'Choose any Timezone', fg = 'blue', font = 'bold')
#         self.listbox_frame = Frame(root, width = 100, height= 200, bg = 'gray')
#         self.scrollbar = Scrollbar(self.listbox_frame, orient = VERTICAL)
#         self.listbox = Listbox(self.listbox_frame, yscrollcommand = self.scrollbar.set)
#         self.timezone_label = Label(root, text = 'final_time', font = 'bold')
#         # self.bttn = Button(root, text = 'get timezone', font = 'bold', command = self.get_timezone)
#     def pack(self):
#         self.title.pack(side = TOP)
#         self.listbox_frame.pack()
#         self.scrollbar.config(command = self.listbox.yview)
#         self.listbox.pack(side = RIGHT, fill = BOTH, expand = 1)
#         self.scrollbar.pack(side = RIGHT, fill = Y)
#         self.timezone_label.pack()
#         # self.bttn.pack()
#     def insert_timezones(self):
#         for i in self.t.timezones:
#             self.listbox.insert(END, i)
#     def get_timezone(self):
#         selection = app.listbox.curselection()
#         # print(selection)
#         for index in selection: 
#             # index = items
#             # print('index: ', index)
#             actual_value = str(self.listbox.get(index))
#             # print('actual value: ', actual_value)
#             timezone = pytz.timezone(actual_value)
#             # print('timezone = ', timezone)
#             current = datetime.now(timezone)
#             # print('current: ', current)
#             fmt= '%A %B %d %Y   %I :%M :%S %p %Z'
#             final_time = current.strftime(fmt)
#             # print('final time', final_time)
#             self.timezone_label.configure(text = final_time)
        

# timezoneApp = Timezone()
# app = UI()
# app.pack()
# app.insert_timezones()

# while True:
#     app.get_timezone()
#     root.update()

#excersise 3
#how to connect insert loop to class phonebook

# class Phonebook:
#     def __init__(self):
#         self.phonebook = {'Ralph Barnhart': '100-6843', 'Janet Jones': '686-4502', 'Chris Meyers': '755-6345', 
#                           'r Barnhart': '100-6843', 'vv Jones': '686-4502', 'v Meyers': '755-6345', 
#                           'Ralph gh': '100-6843', 'Janet e': '686-4502', 'Chris g':'755-6345', 
#                           'Ralph d': '100-6843', 'Janet d': '686-4502', 'd Meyers': '755-6345'}
#     def sort(self):
#         sortedPhonebook = sorted(self.phonebook)    
#         return sortedPhonebook
#     def delete(self, name):
#         self.phonebook.pop(name)
   
#     def printDictionary(self):
#         print('phonebook: ', self.phonebook)

# class UI:
#     def __init__(self):
#         self.p = phonebook
#         self.frame1 = Frame(root, width = 300, height = 80)
#         self.name_label = Label(self.frame1, text = 'Name', font = 'bold')
#         self.name_entry = Entry(self.frame1, text = 'Name!')
#         self.phone_label = Label(self.frame1, text = 'Phone', font = 'bold')
#         self.phone_entry = Entry(self.frame1, text = 'Phone')
#         self.frame2 = Frame(root, width = 300, height = 50)
#         self.add_bttn = Button(self.frame2, text = 'Add', font = 'bold', command = self.add)
#         self.load_bttn = Button(self.frame2, text = 'Load', font = 'bold', command = self.load)
#         self.delete_bttn = Button(self.frame2, text = 'Delete', font = 'bold', command = self.delete)
#         self.update_bttn = Button(self.frame2, text = 'Update', font = 'bold', command = self.update)
#         self.frame3 = Frame(root, width = 300, height = 20)
#         self.scrollbar = Scrollbar(self.frame3, orient = VERTICAL)
#         self.listbox = Listbox(self.frame3, yscrollcommand = self.scrollbar.set)

#     def pack(self):
#         self.frame1.grid(row = 1, column = 1)
#         self.name_label.grid(row = 1, column = 1)
#         self.name_entry.grid(row = 1, column = 2)
#         self.phone_label.grid(row = 2, column = 1)
#         self.phone_entry.grid(row = 2, column = 2)
#         self.frame2.grid(row = 3, column = 1)
#         self.add_bttn.grid(row = 3, column = 1)
#         self.load_bttn.grid(row = 3, column = 2)
#         self.delete_bttn.grid(row = 3, column = 3)
#         self.update_bttn.grid(row = 3, column = 4)
#         self.frame3.grid(row = 4, column = 1)
#         self.scrollbar.grid(row = 4, column =2)
#         self.listbox.grid(row=4, column = 1)
#     def update_listbox(self):
#         self.listbox.delete(0, END)
#         #insert loop
#         sortedPhonebook =self.p.sort()
#         print(sortedPhonebook)
#         for name in sortedPhonebook:
#             self.listbox.insert(END, name)
#     def add(self):
#         name = self.name_entry.get()
#         phonenumber = self.phone_entry.get()
#         self.p.phonebook[name] = phonenumber
#         print(name, phonenumber)
#         self.update_listbox()
#         self.p.printDictionary()
#     def load(self):
#         #get index of chosen contact name
#         selection = self.listbox.curselection()
#         for index in selection: 
#             name = self.listbox.get(index)
#             self.name_entry.delete(0, END)
#             self.name_entry.insert(0, name)
#             phonenumber = self.p.phonebook.get(name)
#             self.phone_entry.delete(0, END)
#             self.phone_entry.insert(0, phonenumber)
#             # print('actual value of index: ', name)
#             # print('phonenumber of name: ', phonenumber)
#     def delete(self):
#         selection = self.listbox.curselection()
#         for index in selection: 
#             name = self.listbox.get(index)
#             print(name)
#             self.p.delete(name)
#             self.p.printDictionary()
#         self.update_listbox()
#     def update(self):
#         self.load()
#         upd_name = self.name_entry.get()
#         upd_phonenumber = self.phone_entry.get()
#         print(upd_name, upd_phonenumber)
#         if len(upd_name) and len(upd_phonenumber) != 0:
#             self.p.phonebook[upd_name] = upd_phonenumber
#             self.update_listbox()
#         else:
#             messagebox.showwarning('show warning', 'pick a contact name to update') 


# phonebook = Phonebook()
# app = UI()
# app.pack()
# app.update_listbox()
# root.mainloop()


#excersise 4

class Login:
    def __init__(self):
        self.login_dictionary = {}
    def getDictionary(self):
        file = open('login_app.txt', 'r')
        for line in file:
            splitLine = line.split()
            username =splitLine[0]
            password =splitLine[1]
            self.login_dictionary[username] = password 
        print(self.login_dictionary)
    def validate(self):
        pass

class UI:
    def __init__(self):
        self.notebook = ttk.Notebook(root)
        self.login_frame = Frame(self.notebook)
        self.register_frame = Frame(self.notebook)
        self.reset_frame = Frame(self.notebook)
        self.unsubscribe_frame = Frame(self.notebook)
        self.username_label = Label(self.login_frame, text = 'Username')
        self.username_entry = Entry(self.login_frame)
        self.password_label = Label(self.login_frame, text = 'Password')
        self.password_entry = Entry(self.login_frame)
        self.submit_bttn = Button(self.login_frame, text = 'Submit')
    def pack(self):
        self.notebook.add(self.login_frame, text = 'Login')
        self.notebook.add(self.register_frame, text = 'Register')
        self.notebook.add(self.reset_frame, text = 'Reset Password')
        self.notebook.add(self.unsubscribe_frame, text = 'Unsubscribe')
        self.notebook.pack()
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.submit_bttn.pack()

    def validate(self):
        pass
    
    

login = Login()
login.getDictionary()
app = UI()
app.pack()
root.mainloop()

