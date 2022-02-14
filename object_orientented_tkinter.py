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

root.geometry('300x200')

answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', '7*3': '21'}
radioButtonList1 = [Radiobutton(root, text = '25', value= 0), Radiobutton(root, text = '20', value= 1)]
radioButtonList2 = [Radiobutton(root, text = 'Washington DC', value= 0), Radiobutton(root, text = 'SF', value= 1)]
questionObjList = []
# for x in range(5):
#     option = Radiobutton(root, text = 'Up', variable = radio_variable, value= 0)
#     radioButtonList.append(option)

score_frame = Frame(root, width = 300, height = 25)
score_label = Label(score_frame, text = 'Score: 0', font = 'bold')
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
        print(questionObjList)
        questionObjList[questionNum]
        self.frame.pack()
        self.question.pack()
        for each in self.options:
            each.pack()

    def hide_question(self):
        self.frame.pack_forget()
        
        
    def submit(self):
        pass

for each in range(2):
    question =  Question(root, Frame(root, bg = 'white'), Label(root, text = str(answerKey()[0]), font = 'bold'), next(iter(answerKey)), IntVar(), radioButtonList1, radioButtonList1[0])
    questionObjList.append(question)


question1 = Question(root, Frame(root, bg = 'white'), Label(root, text = 'what is 5*5?', font = 'bold'), '25', IntVar(), radioButtonList1, radioButtonList1[0])
question2 = Question(root, Frame(root, bg = 'white'), Label(root, text = 'capital of USA?', font = 'bold'), 'Washington DC', IntVar(), radioButtonList2, radioButtonList2[1])

question1.show_question(0)

button_frame = Frame(root, width = 300, height = 25)
button_frame.pack(fill = BOTH)

submit_button = Button(button_frame, text = 'Submit',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = question1.submit)
next_button = Button(button_frame, text = 'Next', width = 7, height = 1, font = 'bold', bg = 'gray', fg = 'white', command = question1.hide_question)
submit_button.pack(side = 'left')
next_button.pack(side = 'right')

root.mainloop()

# question2 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
# question3 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
# question4 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )
# question5 = Question(root, Frame(root), Label(root, text = 'what is 5*5?'), '25', IntVar(), radioButtonList, radioButtonList[0] )



