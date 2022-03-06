import webbrowser
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

#happening in the background
class Quiz:
    def __init__(self):
        self.optionList1 = [Radiobutton(root, text = '25', value= 0), Radiobutton(root, text = '20', value= 1)]
        self.optionList2 = [Radiobutton(root, text = 'Washington DC', value= 0), Radiobutton(root, text = 'SF', value= 1)]
        self.optionList3 = [Radiobutton(root, text = '395 AD', value= 0), Radiobutton(root, text = '455 AD', value= 1)]

        self.questionObjList = []
    def compare_answer():
        pass
    
class UI:
    def __init__(self, root, questionNum, tracker):
        self.answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.r = root
        self.frame =  Frame(root, width = 300, height = 25)
        self.questionNum = questionNum
        self.question = list(self.answerKey.keys())[questionNum]
        self.question_label = Label(self.frame, text = self.question, font = 'bold', fg = 'black') 
        self.answer = list(self.answerKey.values())[questionNum]
        self.answer_label = Label(self.frame, text = self.answer, font = 'bold', fg = 'green')
        self.tracker = tracker
        self.options = [[Radiobutton(self.frame, text = '25', value= 0), Radiobutton(self.frame, text = '20', value= 1)], [Radiobutton(root, text = 'Washington DC', value= 0), Radiobutton(root, text = 'SF', value= 1)], [Radiobutton(root, text = '395 AD', value= 0), Radiobutton(root, text = '455 AD', value= 1)]]
        self.score = 0
        self.score_label = Label(self.frame, text = 'Score: {}'.format(self.score), font = 'bold')
        self.button1 = Button(self.frame, text = 'Next',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = self.next_question)
        self.button2 = Button(self.frame, text = 'Submit',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = self.submit)
    
    def pack_items(self):
        #pack items
        self.score_label.pack()
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
        if self.tracker == 3:
            finish_label = Label(self.frame, text = 'congrats, you\'re finished.', font= 'bold')
            finish_label.pack()
            #how to break here 
        self.tracker += 1

        print('tracker num: ', self.tracker)
        q= questionObjList[self.tracker]
        q.pack_items()
        # if self.tracker == 1:
        #     q1 = questionObjList[0]
        #     q1.pack_items()

    def submit():
        #submit button
        pass

questionObjList = [UI(root, 0, 0), UI(root, 1, 1), UI(root, 2, 2)]
q1 = questionObjList[0]
q1.pack_items()
# q2= UI(root, 1, IntVar())
# q2.pack_items()
quiz = Quiz()
root.mainloop()


#for each in range(2):
    # question =  UI(root, Frame(root, bg = 'white'), Label(root, text = list(answerKey.keys())[1], font = 'bold'), list(answerKey.values())[1], tracker_var2, radioButtonList2, radioButtonList2[0])
    
