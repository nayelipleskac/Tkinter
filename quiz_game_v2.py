from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Quiz Question Game')

root.geometry('300x400')

class Quiz:
    def __init__(self):
        self.s = 0 #score
        self.qa = {'what is 5*5?': '25', 'Capital of USA:': 'Washington DC', 'What year did Rome fall?': '395 AD'}
        self.o = [['25', '20'], ['San Francisco', 'Washington D.C.'], ['395 AD', '405 AD']] #options
        self.q = list(self.qa.keys())
        self.a = list(self.qa.values())
        self.i= 0
        self.answer_index = [0,1,0]

    def return_question(self):
        return self.q[self.i] #current question
    def next_question(self):
        self.i += 1 #increment list index
        print('increasing index here')

    def return_answer(self):
        return self.q[self.i]
    def compare(self, answer):
        print('answer', answer)
        # if self.qa[self.q[self.i]] == answer:
        if self.answer_index[self.i] == answer:
        # if self.a[self.i] == answer:
            self.add_score()
            print('correct answer chosen')
            return True
        else:
            self.subtract_score()
            print('wrong answer chosen')
            return False
    def add_score(self):
        self.s += 1
    def subtract_score(self):
        self.s -=1
    def return_score(self):
        return str(self.s)
    def return_answer1(self):
        return self.o[self.i][0]
    def return_answer2(self):
        return self.o[self.i][1]

    def debug(self):
        print('current index: ', self.i)
        print('current question: ', self.q[self.i])
        print('current answer: ', self.a[self.i])
        print('current score: ', self.s, '\n')
        

class UI:
    def __init__(self, quiz, root):
        self.quiz = quiz 
        self.w = root #window 
        self.frame =  Frame(self.w, width = 400, height = 25)
        self.ql = Label(self.frame, text = self.quiz.q[self.quiz.i], font = 'bold', fg = 'black', width = 500) #question label
        self.tracker = IntVar()
        self.options = [Radiobutton(self.frame, text = self.quiz.o[self.quiz.i][0], value= 0, variable = self.tracker, fg = 'black'), Radiobutton(self.frame, text = self.quiz.o[self.quiz.i][1], value= 1, variable = self.tracker, fg = 'black')]
        self.sl = Label(root, text = 'Score: {}'.format(self.quiz.return_score()), font = 'bold') #score label
        self.btn1 = Button(text = 'Next', width = 7, height= 1, bg = 'blue', font = 'bold', fg = 'white', command = self.next_questionUI)
        self.btn2 = Button(text = 'Submit', width = 7, height= 1, bg = 'blue', font = 'bold', fg = 'white', command = self.compare_answer)
        

    def update_score(self):
        self.sl.configure(text= 'Score: {}'.format(self.quiz.return_score()))

    def next_questionUI(self):
        self.frame.pack_forget()
        #change font color back to black
        for each in self.options:
            each.configure(fg = 'black')
        self.update_score()
        self.quiz.next_question()

        if self.quiz.i == 3:
            #display message box
            print('show message')
            messagebox.showinfo('showinfo', 'congrats, you\'re finished! Your score was {} points'.format(self.quiz.return_score()))
            finish_label = Label(root, text = 'congrats, you\'re finished. ', font= 'bold')
            finish_label.pack()
            
        else: 
            self.ql.configure(text = '{}'.format(self.quiz.return_question()))
            self.options[0].configure(text = '{}'.format(self.quiz.return_answer1()))
            self.options[1].configure(text = '{}'.format(self.quiz.return_answer2()))

        # self.quiz.debug()
        #with incremented index, you can now display a new question  
        
        if self.quiz.i == 3:
            messagebox.showinfo('showinfo', 'congrats, you\'re finished! Your score was {} points'.format(self.quiz.s))
            finish_label = Label(root, text = 'congrats, you\'re finished. ', font= 'bold')
            finish_label.pack()
        else: 
            app1.pack_items()
    def compare_answer(self):
        print('submit bttn is pressed')
        userAnswer = self.tracker.get()
        if self.quiz.compare(userAnswer):
            print('text is green')
            print('correct answer in green ', self.quiz.answer_index[self.quiz.i])
            self.options[self.quiz.answer_index[self.quiz.i]].configure(fg = 'green')
        elif userAnswer != self.quiz.answer_index[self.quiz.i]:
            print('text is red')
            print('incorrect answer in red', userAnswer)
            self.options[userAnswer].configure(fg = 'red')
        self.update_score()
        self.quiz.debug()

    def pack_items(self):
        self.sl.pack()
        self.frame.pack()
        self.ql.pack()
        for each in self.options:
            each.pack()
        self.btn1.pack(side = 'right')
        self.btn2.pack(side = 'left')


quiz = Quiz()

app1 = UI(quiz, root)

print('QUIZ: ', quiz)
print('App: ', app1)
app1.pack_items()
root.mainloop()


