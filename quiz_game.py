import webbrowser
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title('Quiz Question Game')

#happening in the background
class Quiz:
    def __init__(self):
        self.answerKey = {'what is 5*5': '25', 'capital of USA': 'Washington DC', '7*3': '21'}
    def compare_answer():
        pass
    
class UI:
    def __init__(self, root, game, frame, question,answer, tracker, options, answer_index, score):
        self.root = root
        self.g = game
        self.frame =  frame
        self.question = question
        self.answer = answer 
        self.tracker = tracker
        self.options = options
        self.answer_index = answer_index
        self.score = score
        self.score_label = Label(root, text = 'Score: {score}', font = 'bold')
        self.b1 = Button(root, text = 'Next', command = self.next_question)
        self.q1 = UI(root, Frame(root, bg = 'white'), '5*5', '25', IntVar(), , score)
    def pack(self):
        #pack item
        pass
    def next_question():
        pass
    def submit():
        #submit button
        pass




#for each in range(2):
    # question =  UI(root, Frame(root, bg = 'white'), Label(root, text = list(answerKey.keys())[1], font = 'bold'), list(answerKey.values())[1], tracker_var2, radioButtonList2, radioButtonList2[0])
    
