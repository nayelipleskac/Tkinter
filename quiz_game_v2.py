from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

cq = 0

class Quiz:
    def __init__(self, answer_index):
        self.s = 0 #score
        self.qa = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.question = list(self.qa.keys())[cq]
        self.answer = list(self.qa.values())[cq]
        self.cq = IntVar() #current question
        self.answer_index = answer_index

    def compare(self, answer):
        if self.qa[self.cq] == answer:
            self.s = self.s + 1

class UI:
    def __init__(self, root, answer1, answer2, question):
        # self.q = quiz 
        self.q = question 
        self.w = root #window 
        self.frame =  Frame(self.w, width = 300, height = 25)
        self.question_label = Label(self.frame, text = self.q, font = 'bold', fg = 'black')
        self.options = [Radiobutton(self.frame, text = answer1, value= 0, variable = self.q.cq), Radiobutton(self.frame, text = answer2, value= 1, variable = self.q.cq)]
        self.score_label = Label(root, text = 'Score: {}'.format(self.q.s), font = 'bold')
        self.btn1 = Button(text = 'Next', command = self.next_question)
        self.btn2 = Button(text = 'Submit', command = self.q.compare)

    def submit_question(self):
        self.q.compare(self.bttn.get())
        
    def next_question(self):
        pass

    def pack_items(self):
        self.frame.pack()
        self.question_label.pack(side = 'left')
        print('packed_items')


quiz = Quiz(0)
app = UI(root, '20', '25', quiz.question)
print('QUIZ: ', quiz)
print('App: ', app)
app.pack_items()
root.mainloop()



        