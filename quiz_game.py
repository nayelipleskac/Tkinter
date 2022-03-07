from email import message
import webbrowser
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()

score = 0
score_label = Label(root, text = 'Score: {}'.format(score), font = 'bold')

#happening in the background
class Quiz:
    
    def __init__(self):
        self.answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall?': '395 AD'}
       
    def compare_answer(tracker):
        global score
        q= questionObjList[tracker]
        questionNum = tracker
        if questionNum == 0:
            x = btn1.get()
            if x == q.answer: #comparing first q
                score += 1
                #change correct answer to green and change wrong answer to red
                score_label['text'] = 'Score: {}'.format(score)
                print('correct answer chosen')
                print('score: ', score)
            else: 
                print('wrong answer chosen')
        if questionNum == 1:
            x = btn2.get()
            if x == q.answer: #comparing second q
                score += 1
                score_label['text'] = 'Score: {}'.format(score)
                print('correct answer chosen')
                print('score: ', score)
            else: 
                print('wrong answer chosen')
        if questionNum == 2:
            x= btn3.get()
            if x == q.answer: #comparing third q
                score += 1
                score_label['text'] = 'Score: {}'.format(score)
                print('correct answer chosen')
                print('score: ', score)
            else: 
                print('wrong answer chosen')
        root.update()
        # for questions in q:
        #     x = questions.get

 

class UI:
    def __init__(self, root, tracker,):
        self.answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.r = root
        self.frame =  Frame(root, width = 300, height = 25)
        # self.questionNum = questionNum
        self.question = list(self.answerKey.keys())[tracker]
        self.question_label = Label(self.frame, text = self.question, font = 'bold', fg = 'black') 
        self.answer = list(self.answerKey.values())[tracker]
        self.answer_label = Label(self.frame, text = self.answer, font = 'bold', fg = 'green')
        self.tracker = tracker
        self.options = [[Radiobutton(self.frame, text = '25', value= '25', variable = btn1), Radiobutton(self.frame, text = '20', value= '20', variable = btn1)], 
        [Radiobutton(self.frame, text = 'Washington DC', value= 'Washington DC', variable = btn2), Radiobutton(self.frame, text = 'SF', value= 'SF', variable = btn2)], 
        [Radiobutton(self.frame, text = '395 AD', value= '395 AD', variable = btn3), Radiobutton(self.frame, text = '455 AD', value= '455 AD', variable = btn3)]]
        self.button1 = Button(self.frame, text = 'Next',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = self.next_question)
        self.button2 = Button(self.frame, text = 'Submit',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = self.submit)
    
    def pack_items(self):
        #pack items
        score_label.pack()
        self.frame.pack()
        self.question_label.pack()
        for each in self.options[self.tracker]:
            each.pack()
        self.button1.pack(side = 'left')
        self.button2.pack(side = 'right')
        self.answer_label.pack()

        
    def hide_question(self):
        self.frame.pack_forget()
    def next_question(self):
        self.hide_question()
        self.tracker += 1
        if self.tracker == 3:
            messagebox.showinfo('showinfo', 'congrats, you\'re finished! Your score was {} points'.format(score))
            # self.hide_question()
            finish_label = Label(root, text = 'congrats, you\'re finished. ', font= 'bold')
            finish_label.pack()
        else:           
            print('tracker num: ', self.tracker)
            q= questionObjList[self.tracker]
            q.pack_items()

    def submit(self):
        #submit button

        Quiz.compare_answer(self.tracker)

questionObjList = [UI(root, 0), UI(root, 1), UI(root, 2)]
q1 = questionObjList[0]
q1.pack_items()

quiz = Quiz()
root.mainloop()


    
