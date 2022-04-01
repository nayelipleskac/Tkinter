from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

class Quiz:
    def __init__(self):
        self.s = 0 #score
        self.qa = {'what is 5*5?': '25', 'Capital of USA:': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.o = {'what is 5*5?': ['25', '20'], 'Capital of USA': ['San Franciso', 'Washington D.C.'], 'What year did Rome fall?': ['395 AD', '405 AD']}
        self.q = list(self.qa.keys())
        self.a = list(self.qa.values())
        self.i= 0
    def return_question(self):
        return self.q[self.i] #current question
    def next_question(self):
        self.i += 1 #increment list index
    def return_answer(self):
        return self.q[self.i]
    def compare(self, answer):
        # if self.qa[self.q[self.i]] == answer:
        if self.a[self.i] == answer:
            self.s = self.s + 1
    def add_score(self):
        self.s += 1
    def subtract_score(self):
        self.s -=1
    def return_score(self):
        return str(self.s)
    def return_answer1(self):
        return self.o[self.q[self.i]][0]
    def return_answer2(self):
        return self.o[self.q[self.i]][1] 

    def debug(self):
        print('current question: ', self.q[self.i])
        print('current answer: ', self.a[self.i])
        print('current score: ', self.s[self.i])



class UI:
    def __init__(self, quiz, root, answer_index):
        self.quiz = quiz 
        self.w = root #window 
        self.frame =  Frame(self.w, width = 400, height = 25)
        self.ql = Label(self.frame, text = self.quiz.q[self.quiz.i], font = 'bold', fg = 'black', width = 500) #question label
        self.options = [Radiobutton(self.frame, text = ''.format(self.quiz.return_answer1()), value= 0, variable = self.quiz.i), Radiobutton(self.frame, text = ''.format(self.quiz.return_answer1()), value= 1, variable = self.quiz.i)]
        self.sl = Label(root, text = 'Score: {}'.format(self.quiz.return_score()), font = 'bold') #score label
        self.btn1 = Button(text = 'Next', width = 7, height= 1, bg = 'blue', font = 'bold', fg = 'white', command = self.next_question1)
        self.btn2 = Button(text = 'Submit', width = 7, height= 1, bg = 'blue', font = 'bold', fg = 'white', command = self.compare_answer)
        self.answer_index = answer_index

    def update_score(self):
        self.sl.configure(text= 'Score: {}'.format(self.quiz.return_score()))

    def next_question1(self):
        #quiz.next_question gets return values after
        #unpack and pack
        self.frame.pack_forget()
        self.quiz.next_question()
        self.ql.configure(text = '{}'.format(self.quiz.return_question()))
        #with incremented index, you can now display a new question
        
        if self.quiz.i == 3:
            messagebox.showinfo('showinfo', 'congrats, you\'re finished! Your score was {} points'.format(self.quiz.s))
            finish_label = Label(root, text = 'congrats, you\'re finished. ', font= 'bold')
            finish_label.pack()
        else: 
            # self.question_label.pack()
            app.pack_items()
    def compare_answer(self):
        #update score and color of answer text
        self.quiz.compare()

    def pack_items(self):
        self.sl.pack()
        self.frame.pack()
        self.ql.pack()
        print(self.ql)
        for each in self.options:
            each.pack()
        self.btn1.pack(side = 'right')
        self.btn2.pack(side = 'left')


quiz = Quiz()

app = UI(quiz, root, 1)

print('QUIZ: ', quiz)
print('App: ', app)
app.pack_items()
root.mainloop()



          #next_question function increments current index and returns question and answer   