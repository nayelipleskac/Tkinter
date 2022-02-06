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

# import random, string
# password = ''
# def submit():
#     global password
#     a = radio_variable.get()
#     b = current_val.get()
#     letters = string.ascii_lowercase
#     numbers = string.digits
#     special_chr = string.punctuation
#     print('radio choice ', a, 'password length ', b)
#     if a == 0: #low
#         low_password = ''.join(random.choice(letters) for i in range(b))
#         print(low_password)
#         password = low_password
#         label2['text'] = low_password
#         root.update()
        
#     if a == 1: #mid
#         mid_password = ''.join(random.choice(letters + numbers) for i in range(b))
#         print(mid_password)
#         password = mid_password
#         label2['text'] = mid_password


#     if a == 2: #high
#         high_password = ''.join(random.choice(letters + numbers + special_chr) for i in range(b))
#         print(high_password)
#         password = high_password
#         label2['text'] = high_password

    
# root.geometry('300x200')
# frame1 = Frame(root, width = 400, height = 50)
# frame1.pack(fill = BOTH)

# frame2 = Frame(root, width = 200, height = 50)
# frame2.pack(fill = BOTH)
# frame3 = Frame(root, width = 200, height = 50)
# frame3.pack(fill = BOTH)
# frame4 = Frame(root, width = 200, height = 50)
# frame4.pack(fill = BOTH)

# # password = 
# label1 = Label(frame1, text= 'Generated Password: ',fg = 'blue').grid(row = 1, column = 1)
# label2 = Label(frame1, textvariable = password, fg = 'black')
# label2.grid(row = 1, column = 2)

# label3 = Label(frame2, text= 'Password Strength: ')
# label3.grid(row = 2, column = 1)
# #three radios
# radio_variable = IntVar()
# radio_low = Radiobutton(frame2, text = 'Low', variable = radio_variable, value= 0)
# radio_low.grid(row =2, column = 2)
# radio_mid = Radiobutton(frame2, text = 'Medium', variable = radio_variable, value= 1)
# radio_mid.grid(row = 3, column = 2)
# radio_high = Radiobutton(frame2, text = 'High', variable = radio_variable, value= 2)
# radio_high.grid(row = 4, column = 2)

# label4 = Label(frame3, text= 'Password Length: ')
# label4.grid(row = 5, column = 1)
# current_val = IntVar()
# password_length = Spinbox(frame3, from_ = 6, to= 12, textvariable = current_val).grid(row = 5, column = 2)
# submit_bttn = Button(frame4, text = 'Submit', command = submit, bg = 'green', fg = 'white').grid(row = 6, column = 2)

# root.mainloop()


#login-app
password_ = 'magic'

def showPassword():
    a = check_var.get()
    if a == 1: #selected 
        print('here!')
        entry2.config(show = "")
    else: 
        entry2.config(show = "*")

def login():
    # global password_
    remember_box = remember_var.get()
    terms_box = terms_var.get()
    # terms_bttn= terms.get()
    username_entry = entry1.get()
    password_entry = entry2.get()

    if remember_box == 1:
        info = str([username_entry, password_entry])
        f = open('userinfo.txt', 'w')
        f.write(info)
        f.close()
        print(info)
    if terms_box == 1:
        print('successfully logged in!')
        terms['fg'] = 'green'
    if terms_box== 0:
        terms['fg'] = 'red'

root.geometry('300x200')
frame1 = Frame(root, width = 200, height = 50)
frame1.pack(fill = BOTH)
frame2 = Frame(root, width = 200, height = 50)
frame2.pack(fill = BOTH)
frame3 = Frame(root, width = 200, height = 50)
frame3.pack(fill = BOTH)
frame4 = Frame(root, width = 200, height = 50)
frame4.pack(fill = BOTH)
frame5 = Frame(root, width = 200, height = 50)
frame5.pack(fill = BOTH)
frame6 = Frame(root, width = 200, height = 50)
frame6.pack(fill = BOTH)

label1 = Label(frame1, text= 'Username: ',fg = 'black').grid(row = 1, column = 1)
label2 = Label(frame1, fg = 'black')
label2.grid(row = 1, column = 2)

entry1 = Entry(frame1)
entry1.grid(row = 1, column = 2)

label3 = Label(frame2, text= 'Password: ')
label3.grid(row = 2, column = 1)
entry2 = Entry(frame2, show = "*")
entry2.grid(row = 2, column = 2)

check_var = IntVar()
remember_var = IntVar()
terms_var=  IntVar()
check_password = Checkbutton(frame3, text= 'Show Password', variable = check_var, command = showPassword)
check_password.grid(row = 3, column = 2)

remember_password = Checkbutton(frame4, text= 'Remember Password', fg = 'blue', variable = remember_var)
remember_password.grid(row = 4, column = 1)

terms = Checkbutton(frame5, text= 'I accept the terms and conditions', fg = 'blue', variable = terms_var)
terms.grid(row = 5, column = 1)

login_bttn = Button(frame6, text = 'Login', fg = 'black', bg = 'gray', width = 15, command = login)
login_bttn.grid(row = 6, column = 1, )

root.mainloop()

