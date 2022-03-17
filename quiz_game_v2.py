from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

class UI:
    def __init__(self, root):
        self.w = root #window 
        self.q = Quiz 
        self.frame =  Frame(root, width = 300, height = 25)
        self.question_label = Label(self.frame, text = Quiz.question, font = 'bold', fg = 'black')
        # self.options = [Radiobutton(self.frame, text = answer1, value= 0, variable = self.q.cq), Radiobutton(self.frame, text = answer2, value= 1, variable = self.q.cq)]
        # self.score_label = Label(root, text = 'Score: {}'.format(self.q.score), font = 'bold')
        self.btn1 = Button(text = 'Next', command = self.next_question)
        self.btn2 = Button(text = 'Submit', command = self.q.compare)
    def submit_question(self):
        #getting user's choice from options
        #user's choice
        self.q.compare(self.bttn.get())
    def next_question(self):
        pass
    def pack_items(self):
        self.question_label.pack()



class Quiz:
    def __init__(self):
        self.s = 0 #score
        self.qa = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.cq = cq #current question
        self.question = list(self.qa.keys())[self.cq]
        # self.answer = list(self.qa.values())[self.cq]
        # self.answer_index = answer_index

    def compare(self, answer):
        if self.qa[self.cq] == answer:
            self.s = self.s + 1

quiz = Quiz()
app = UI(root)
root.mainloop()



        