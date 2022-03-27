#set 4
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

colors = ['red', 'green', 'blue', 'purple']

title = Label(root, text = 'COLORS')
title.grid(row = 0, column = 0)

color_label = Label(root, bg = 'green')
color_label.grid(row = 2, column = 0)

#creating a Listbox
listbox_1 = Listbox(root)
listbox_1.grid(row = 1, column = 0)

def get_index():
    print('get_index')
    selection = listbox_1.curselection()
    for item in selection:
        print('you have selected index ' + str(item))
        index = str(item)
        actual_value = listbox_1.get(index)
        print(actual_value, ' actualvalue')
        # print('selection index ', selection[item])


#append a value to the Listbox
for i in colors:
    listbox_1.insert(END, i)

button = Button(root, text = 'submit', command= get_index)
button.grid(row = 3, column = 1)
root.mainloop()

# while True:
#     #to get index of selected items
#     selection = listbox_1.curselection()
#     print('selection', selection)
#     if len(selection) > 0:
#         index = selection[0]
#         print('index ', index)

    # #to get the value from the listbox based on index 
    # actual_value = listbox_1.get(index)



