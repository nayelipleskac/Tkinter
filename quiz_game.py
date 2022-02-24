import webbrowser
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')


#happening in the background
class Quiz:
    def __init__(self):
        self.answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', 'What year did Rome fall': '395 AD'}
        self.optionList1 = [Radiobutton(root, text = '25', value= 0), Radiobutton(root, text = '20', value= 1)]
        self.optionList2 = [Radiobutton(root, text = 'Washington DC', value= 0), Radiobutton(root, text = 'SF', value= 1)]
        self.optionList3 = [Radiobutton(root, text = '395 AD', value= 0), Radiobutton(root, text = '455 AD', value= 1)]

        self.questionObjList = []
    def compare_answer():
        pass
    
class UI:
    def __init__(self, root, game, frame, question, answer, tracker, options, answer_index):
        self.root = root
        self.g = game
        self.frame =  Frame(root, width = 300, height = 25)
        self.question = question
        self.answer = answer 
        self.tracker = tracker
        self.options = options
        self.answer_index = ['25', 'Washinton', '395 AD']
        self.score = 0
        self.score_label = Label(root, text = 'Score: {score}', font = 'bold')
        self.b1 = Button(frame, text = 'Next',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = self.next_question)
        self.b2 = Button(frame, text = 'Submit',  width = 7, height= 1, bg = 'gray', font = 'bold', fg = 'white', command = self.submit)
    
    def pack(self):
        #pack items
        self.score_label.pack()
        self.frame.pack()
        self.b1.pack(side = 'left')
        self.b2(side = 'right')
    def next_question(self):
        self.frame.pack_forget()
        

    def submit():
        #submit button
        pass

app = UI()
quiz = Quiz()
root.mainloop()


#for each in range(2):
    # question =  UI(root, Frame(root, bg = 'white'), Label(root, text = list(answerKey.keys())[1], font = 'bold'), list(answerKey.values())[1], tracker_var2, radioButtonList2, radioButtonList2[0])
    
