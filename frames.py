import tkinter as tk
from tkinter import Button, Entry, Frame, Label, StringVar, IntVar, messagebox
from tkinter.constants import END, LEFT, RIGHT, TOP
root =  tk.Tk()
root.title('Cart')

vertical_frame = Frame(root,width =50, height = 150, bg = 'black')
vertical_frame.pack()

horizontal_frame = Frame(root, width =150, height = 50, bg = 'red')
horizontal_frame.pack()


root.mainloop()
