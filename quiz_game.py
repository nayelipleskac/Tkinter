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

tracker = 0

score = 0
score_label = Label(root, text = 'Score: {}'.format(score), font = 'bold')

def compare_answer():
    global score, tracker
    q= questionObjList[tracker]
    # questionNum = tracker

    x = q.tracker.get()
    if x == q.answer_index: #comparing first q
        score += 1
        #change correct answer to green and change wrong answer to red
        print('q.answer', q.answer)
        q.options[q.answer_index].configure(fg = 'green') 
        # q.options[]
        score_label['text'] = 'Score: {}'.format(score)
        print('correct answer chosen')
        print('score: ', score)
    else: 
        print('wrong answer chosen')
    
    root.update()
   

class UI:
    def __init__(self, root, tracker, answer1, answer2, answer_index):
        self.answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.r = root
        self.frame =  Frame(root, width = 300, height = 25)
        # self.questionNum = questionNum
        self.question = list(self.answerKey.keys())[tracker]
        self.question_label = Label(self.frame, text = self.question, font = 'bold', fg = 'black') 
        self.answer = list(self.answerKey.values())[tracker]
        self.answer_label = Label(self.frame, text = self.answer, font = 'bold', fg = 'green')
        self.tracker = IntVar()
        self.options = [Radiobutton(self.frame, text = answer1, value= 0, variable = self.tracker), Radiobutton(self.frame, text = answer2, value= 1, variable = self.tracker)]

        self.answer_index = answer_index
    
    def pack_items(self):
        #pack items
        score_label.pack()
        self.frame.pack()
        self.question_label.pack()
        for each in self.options:
            each.pack()

def next_question():
    global tracker
    q= questionObjList[tracker]
    q.frame.pack_forget()
    tracker += 1
    if tracker == 3:
        messagebox.showinfo('showinfo', 'congrats, you\'re finished! Your score was {} points'.format(score))
        # self.hide_question()
        finish_label = Label(root, text = 'congrats, you\'re finished. ', font= 'bold')
        finish_label.pack()
    else:           
        print('tracker num: ', tracker)
        q= questionObjList[tracker]
        q.pack_items()


questionObjList = [UI(root, 0, '25', '20', 0), UI(root, 1,'SF', 'Washington DC', 1), UI(root, 2, '486 AD','395 AD', 1)]
q1 = questionObjList[0]
# q2 = questionObjList[0]
bttn_frame = Frame(root, width = 300, height = 25)
bttn_frame.pack()
button1 = Button(bttn_frame, text = 'Next',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = next_question)
button2 = Button(bttn_frame, text = 'Submit',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = compare_answer)
button1.pack(side = 'left')
button2.pack(side = 'right')

q1.pack_items()
# q2.pack_items()
root.mainloop()


    
