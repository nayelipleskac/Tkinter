from gettext import find
import tkinter as tk
import pygame 
pygame.init()
from tkinter import BOTH, Button, Checkbutton, Entry, Frame, Image, Label, PhotoImage, Radiobutton, Spinbox, StringVar, IntVar, messagebox
from tkinter.constants import END, LEFT, RIGHT, TOP
root =  tk.Tk()

root.title('Buttons')

#reg button
# regular_btton = Button(root, text = 'Find', command = find)
# # regular_btton.pack()
# #check button
# regex_variable = IntVar()
# match_variable = IntVar()
# check_regular_expression = Checkbutton(root, text= 'Regular Button', variable = regex_variable)
# check_regular_expression.pack()
# check_match_case = Checkbutton(root, text = 'Match case', variable= match_variable)
# check_match_case.pack()

# #radio buttons
# radio_variable = IntVar()
# radio_up = Radiobutton(root, text = 'Up', variable = radio_variable, value= 0)
# radio_up.pack()
# radio_down = Radiobutton(root, text = 'Down', variable = radio_variable, value= 1)
# radio_down.pack()

#Registration form

# def submit():
#     a = name_entry.get()
#     b = age_entry.get()
#     c = radio_variable.get()
#     info = a+ b+ str(c)
#     f = open('studentinfo.txt', 'w')
#     f.write(info)
#     f.close()
#     print(a, b,'level: ', c)


# name_title = Label(root, text = 'Name')
# name_title.grid(column = 1, row = 1)
# name_entry = Entry(root, text = 'Name')
# name_entry.grid(column =2, row = 1)

# age_title = Label(root, text = 'Age')
# age_title.grid(column = 1, row = 2)
# age_entry = Entry(root, text = 'Age')
# age_entry.grid(column =2, row = 2)

# level_label = Label(root, text = 'Choose your Level')
# level_label.grid(row = 3, column = 2)
# radio_variable = IntVar()
# radio_0 = Radiobutton(root, text = 'Level 0', variable = radio_variable, value= 0)
# radio_0.grid(row = 4, column = 2)
# radio_1 = Radiobutton(root, text = 'Level 1', variable = radio_variable, value= 1)
# radio_1.grid(row= 5, column = 2)
# radio_2 = Radiobutton(root, text = 'Level 2', variable = radio_variable, value= 2)
# radio_2.grid(row = 6, column = 2)
# radio_3 = Radiobutton(root, text = 'Level 3', variable = radio_variable, value= 3)
# radio_3.grid(row= 7, column = 2)
# radio_4 = Radiobutton(root, text = 'Level 4', variable = radio_variable, value= 4)
# radio_4.grid(row = 8, column = 2)
# radio_5 = Radiobutton(root, text = 'Level 5', variable = radio_variable, value= 5)
# radio_5.grid(row= 9, column = 2)

# submit_button = Button(root, text = 'Submit', command = submit, bg = 'blue', fg = 'white')
# submit_button.grid(row = 10, column = 2)

# root.mainloop()

def submit():
    print('submit!!')
    radio_variable.get()
    password_length.get()

root.geometry('300x200')
frame1 = Frame(root, width = 200, height = 50)
frame1.pack(fill = BOTH)

frame2 = Frame(root, width = 200, height = 50)
frame2.pack(fill = BOTH)
frame3 = Frame(root, width = 200, height = 50)
frame3.pack(fill = BOTH)
frame4 = Frame(root, width = 200, height = 50)
frame4.pack(fill = BOTH)

password = 'password'
label1 = Label(frame1, text= 'Generated Password: ',fg = 'blue').grid(row = 1, column = 1)
label2 = Label(frame1, text = password, fg = 'black').grid(row = 1, column = 2)

label3 = Label(frame2, text= 'Password Strength: ').grid(row = 2, column = 1)
#three radios
radio_variable = IntVar()
radio_low = Radiobutton(frame2, text = 'Low', variable = radio_variable, value= 0)
radio_low.grid(row =2, column = 2)
radio_mid = Radiobutton(frame2, text = 'Medium', variable = radio_variable, value= 1)
radio_mid.grid(row = 3, column = 2)
radio_high = Radiobutton(frame2, text = 'High', variable = radio_variable, value= 2)
radio_high.grid(row = 4, column = 2)

label4 = Label(frame3, text= 'Password Length: ').grid(row = 5, column = 1)
password_length = Spinbox(frame3, from_ = 6, to= 12).grid(row = 5, column = 2)
submit_bttn = Button(frame4, text = 'Submit', command = submit, bg = 'green', fg = 'white').grid(row = 6, column = 2)


root.mainloop()