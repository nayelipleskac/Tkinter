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

radioButtonList = [Radiobutton(root, text = '25', value= 0), Radiobutton(root, text = '20', value= 1)]

# for x in range(5):
#     option = Radiobutton(root, text = 'Up', variable = radio_variable, value= 0)
#     radioButtonList.append(option)

class Question():
    def __init__(self, root, frame, question, answer, tracker, options, answer_index):
        self.root = root
        self.frame = frame
        self.question = question
        self.answer = answer 
        self.tracker = tracker
        self.options = options
        self.answer_index = answer_index
        
        
    def clicker(self):
        print('you clicked the button!')

question1 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
question1.pack(pady = 20)
root.mainloop()

# question2 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
# question3 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
# question4 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
# question5 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )



