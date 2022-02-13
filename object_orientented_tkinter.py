from cgitb import text
from gettext import find
from select import select
import tkinter as tk
import pygame 
pygame.init()
from tkinter import BOTH, Button, Checkbutton, Entry, Frame, Image, Label, PhotoImage, Radiobutton, Spinbox, StringVar, IntVar, messagebox
from tkinter.constants import END, LEFT, RIGHT, TOP
root =  tk.Tk()

root.title('OO tkinter')

root.geometry('300x500')

radioButtonList = []

# for x in range(5):
#     option = Radiobutton(root, text = 'Up', variable = radio_variable, value= 0)
#     radioButtonList.append(option)

class Question():
    def __init__(self, master, frame, question, answer, tracker, options):
        self.frame = Frame(master)
        self.question = Label(self.frame)
        self.answer = '2'
        self.tracker = IntVar()
        self.options = radioButtonList
    def clicker(self):
        print('you clicked the button!')

question1 = Question(root)

root.mainloop()