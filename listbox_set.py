#set 4
from tkinter import *
from tkinter import messagebox
import pytz, random
from datetime import datetime
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

# excsise 1
# colors = ['red', 'green', 'blue', 'purple']

# title = Label(root, text = 'COLORS')
# title.grid(row = 0, column = 0)

# color_label = Label(root, bg = 'white', width = 8)
# color_label.grid(row = 2, column = 0)

# #creating a Listbox
# listbox_1 = Listbox(root)
# listbox_1.grid(row = 1, column = 0)

# def change_color():
#     print('get_index')
#     selection = listbox_1.curselection()
#     for item in selection:
#         print('you have selected index ' + str(item))
#         index = str(item)
#         actual_value = listbox_1.get(index)
#         #change color_label bg
#         color_label.configure(bg = actual_value)
#         print(actual_value, ' = actual value')
#         # print('selection index ', selection[item])


# #append a value to the Listbox
# for i in colors:
#     listbox_1.insert(END, i)

# button = Button(root, text = 'submit', command= change_color)
# button.grid(row = 3, column = 1)
# root.mainloop()

#exercise 2
timezones = pytz.all_timezones

title = Label(root, text = 'Choose any Timezone', fg = 'blue', font = 'bold')
title.pack(side = TOP)

listbox_frame = Frame(root, width = 100, height= 200, bg = 'gray')
listbox_frame.pack()

scrollbar_1 = Scrollbar(listbox_frame, orient = VERTICAL)
listbox_1 = Listbox(listbox_frame, yscrollcommand = scrollbar_1.set)

scrollbar_1.config(command = listbox_1.yview)
listbox_1.pack(side = RIGHT, fill = BOTH, expand = 1)
scrollbar_1.pack(side = RIGHT, fill = Y)


def get_index():
    selection = listbox_1.curselection()
    for items in selection: 
        index = str(items)
        actual_value = listbox_1.get(index)
        timezone = pytz.timezone(index)
        current = datetime.now(timezone)
        final_time = current.strftime('%d %b %Y %l:%M:%S %p %Z')
        print('index: ', index)
        print('actual value: ', actual_value)
        print('timezone = ', timezone)

timezone_label = Label(root, text = final_time, font = 'bold')
timezone_label.pack()

button = Button(root, text = 'submit', command= get_index)
button.pack()

#append values to listbox_1
for i in timezones:
    listbox_1.insert(END, i)

#get index of user selection 
while True: 
    selection = listbox_1.curselection()
    for items in selection: 
        index = str(items)
        actual_value = listbox_1.get(index)
        timezone = pytz.timezone(index)
        current = datetime.now(timezone)
        final_time = current.strftime('%d %b %Y %l:%M:%S %p %Z')
        print('index: ', index)
        print('actual value: ', actual_value)
        print('timezone = ', timezone)
    

    root.mainloop()

