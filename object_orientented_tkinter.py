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

root.geometry('300x400')

answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', '7*3': '21'}
radioButtonList1 = [Radiobutton(root, text = '25', value= 0), Radiobutton(root, text = '20', value= 1)]
radioButtonList2 = [Radiobutton(root, text = 'Washington DC', value= 0), Radiobutton(root, text = 'SF', value= 1)]
questionObjList = []
# for x in range(5):
#     option = Radiobutton(root, text = 'Up', variable = radio_variable, value= 0)
#     radioButtonList.append(option)

score_frame = Frame(root, width = 300, height = 25)
score_var = 0
score_label = Label(score_frame, text = 'Score: {score_var}', font = 'bold')
score_frame.pack(fill = BOTH)
score_label.pack()

class Question():
    def __init__(self, root, frame, question, answer, tracker, options, answer_index):
        self.root = root
        self.frame =  frame
        self.question = question
        self.answer = answer 
        self.tracker = tracker
        self.options = options
        self.answer_index = answer_index
    def show_question(self, questionNum):
        print('questionObjList: ', questionObjList)
        # questionObjList[questionNum]
        self.frame.pack()
        self.question.pack()
        for each in self.options:
            each.pack()

    def next_question(self):
        global question
        self.frame.pack_forget()
        root.update()
        print('next button was pressed')
        tracker_var2 = IntVar()
        question =  Question(root, Frame(root, bg = 'white'), Label(root, text = list(answerKey.keys())[1], font = 'bold'), list(answerKey.values())[1], tracker_var2, radioButtonList2, radioButtonList2[0])
        questionObjList.append(question)
        question.show_question(each)

        question.show_buttons()
        
    def show_buttons(self):
        button_frame = Frame(root, width = 300, height = 25)
        button_frame.pack(fill = BOTH)
        submit_button = Button(button_frame, text = 'Submit',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = question.submit)
        next_button = Button(button_frame, text = 'Next', width = 7, height = 1, font = 'bold', bg = 'gray', fg = 'white', command = question.next_question)
        submit_button.pack(side = 'left')
        next_button.pack(side = 'right')

    def submit(self):
        #turn correct answer green
        first_question = questionObjList[0]
        first_question.label['fg'] = 'green'

for each in range(2):
    if each == 0:
        tracker_var = IntVar()
        question =  Question(root, Frame(root, bg = 'white'), Label(root, text = list(answerKey.keys())[0], font = 'bold', fg = 'black'), list(answerKey.values())[0], tracker_var, radioButtonList1, radioButtonList1[0])
        questionObjList.append(question)
        question.show_question(each)
        

question.show_buttons()
root.mainloop()








