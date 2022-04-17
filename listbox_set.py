#set 4
from tkinter import *
from tkinter import messagebox
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

class Phonebook:
    def __init__(self):
        pass


class UI:
    def __init__(self):
        self.frame1 = Frame(root, width = 300, height = 50, bg = 'gray')
        self.name_label = Label(self.frame1, text = 'Name', font = 'bold')
        self.name_entry = Entry(self.frame1, text = 'Name')
        self.phone_label = Label(self.frame1, text = 'Phone', font = 'bold')
        self.phone_entry = Entry(self.frame1, text = 'Phone')
        self.frame2 = Frame(root, width = 300, height = 50)
        self.add_bttn = Button(self.frame2, text = 'Add')
        self.load_bttn = Button(self.frame2, text = 'Load')
        self.delete_bttn = Button(self.frame2, text = 'Delete')
        self.update_bttn = Button(self.frame2, text = 'Update')

    def pack(self):
        self.frame1.pack()
        self.name_label.pack(side = 'left')
        self.name_entry.pack()
        self.phone_label.pack(side = 'left')
        self.phone_entry.pack()
        self.frame2.pack()
        self.add_bttn.pack(expand = True)
        self.load_bttn.pack(expand = True)
        self.delete_bttn.pack(expand =True)
        self.update_bttn.pack(expand = True)

phonebook = Phonebook()
app = UI()
app.pack()
root.mainloop()

        
