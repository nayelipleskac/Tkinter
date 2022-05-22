from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd
import wikipedia
root = Tk()
root.title('Custom Notebook App')

root.geometry('400x400')

root = Tk()

l1 = Label(root, text="hello")
l2 = Label(root, text="world")
f1 = Frame(root)
b1 = Button(f1, text="One button")
b2 = Button(f1, text="Another button")
b3 = Button(f1, text="Another button again")


l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
f1.grid(row=1, column=1, sticky="nsew")

b1.pack(side="left")
b2.pack(side = 'top')
b3.pack(side = 'right')

root.mainloop()