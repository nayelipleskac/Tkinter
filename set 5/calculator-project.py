#set 6  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd

root = Tk()
root.title('Calculator Project')

root.geometry('200x250')

#create a grid function for placing btns
class Calculator(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.numList = []
        self.operandsList = []

        self.output_screen = OutputScreen(self)
        # self.output_screen.grid(row  = 0, column = 0)
        self.keypadFrame = Frame(self)
        self.entryFrame = Frame(self)
        # self.historyFrame = Frame(self)

        self.clearbtn = Clear(self.entryFrame)
        self.clearbtn.grid(row = 0, column = 3)
        self.entrybox = Entry(self.entryFrame)
        self.entrybox.grid(row = 0, column =0, columnspan = 3)

        self.btn1 = One(self.keypadFrame)
        self.btn1.grid(row = 0, column = 0)
        # self.btn2 = Two(self.keypadFrame)
        # self.btn2.grid(row = 0, column = 1)
        # self.btn3 = Three(self.keypadFrame)
        # self.btn3.grid(row = 0, column = 2)
        # self.btn4 = Four(self.keypadFrame)
        # self.btn4.grid(row = 1, column = 0)
        # self.btn5 = Five(self.keypadFrame)
        # self.btn5.grid(row = 1, column = 1)
        # self.btn6 = Six(self.keypadFrame)
        # self.btn6.grid(row = 1, column = 2)
        # self.btn7 = Seven(self.keypadFrame)
        # self.btn7.grid(row = 2, column = 0)
        # self.btn8 = Eight(self.keypadFrame)
        # self.btn8.grid(row = 2, column = 1)
        # self.btn9 = Nine(self.keypadFrame)
        # self.btn9.grid(row = 2, column =2)
        # self.btn0 = Zero(self.keypadFrame)
        # self.btn0.grid(row = 3, column = 1)

        # self.addbtn = Add(self.keypadFrame)
        # self.addbtn.grid(row = 0, column = 3)
        # self.subtractbtn = Subtract(self.keypadFrame)
        # self.subtractbtn.grid(row = 1, column = 3)
        # self.multiplybtn = Multiply(self.keypadFrame)
        # self.multiplybtn.grid(row = 2, column = 3)
        # self.dividebtn = Divide(self.keypadFrame)
        # self.dividebtn.grid(row = 3, column= 3)
        # self.equalbtn = Equal(self.keypadFrame)
        # self.equalbtn.grid(row = 3, column = 2)
        # self.decimalbtn = Decimal(self.keypadFrame)
        # self.decimalbtn.grid(row = 3, column = 0)

    def grid(self):
        pass


    def insertValue(self, target):
        self.t = None
        if target == '1':
            self.numList.append(self.btn1.value())
        if target == '2':
            self.numList.append(self.btn2.value())
        if target == '3':
            self.numList.append(self.btn3.value())
        if target == '4':
            self.numList.append(self.btn4.value())
        if target == '5':
            self.numList.append(self.btn5.value())
        if target == '6':
            self.numList.append(self.btn6.value())
        if target == '7':
            self.numList.append(self.btn7.value())
        if target == '8':
            self.numList.append(self.btn8.value())
        if target == '9':
            self.numList.append(self.btn9.value())
        if target == '0':
            self.numList.append(self.btn0.value())
        
        if target == '+':
            self.operandsList.append(self.addbtn.value())
        if target == '-':
            self.operandsList.append(self.subtractbtn.value())
        if target == '*':
            self.operandsList.append(self.multiplybtn.value())
        if target == '/':
            self.operandsList.append(self.dividebtn.value())
        if target == '=':
            self.operandsList.append(self.equalbtn.value())
        if target == '.': 
            self.operandsList.append(self.decimalbtn.value())
        if target == 'C':
            #clear entry box
            print('user has cleared entry box')
        self.debug()

    def add(self, num1, num2):
        pass
    def subtract(self, num1, num2):
        pass
    def multiply(self, num1, num2):
        pass
    def divide(self, num1, num2):
        pass
  
    def debug(self):
        print('numList: ', self.numList)
        print('operands: ', self.operandsList)

class OutputScreen(Text):
    def __init__(self, master):
        self.g = master
        Text.__init__(self, height = 3, width = 25)


class One(Button):
    def __init__(self, master, ):
        self.g = master #calc
        self.n = 1
        Button.__init__(self, command= lambda: self.g.insertValue('1'), height= 3, width = 5, text = self.n )
    def value(self):
        return self.n


class Two(Button):
    def __init__(self, master):
        self.g = master
        self.n = 2
        Button.__init__(self, command = lambda: self.g.insertValue('2'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Three(Button):
    def __init__(self, master):
        self.g = master
        self.n = 3
        Button.__init__(self, command = lambda: self.g.insertValue('3'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Four(Button):
    def __init__(self, master):
        self.g = master
        self.n = 4
        Button.__init__(self, command = lambda: self.g.insertValue('4'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Five(Button):
    def __init__(self, master):
        self.g = master
        self.n = 5
        Button.__init__(self, command = lambda: self.g.insertValue('5'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Six(Button):
    def __init__(self, master):
        self.g = master
        self.n = 6
        Button.__init__(self, command = lambda: self.g.insertValue('6'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Seven(Button):
    def __init__(self, master):
        self.g = master
        self.n = 7
        Button.__init__(self, command = lambda: self.g.insertValue('7'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n
class Eight(Button):
    def __init__(self, master):
        self.g = master
        self.n = 8
        Button.__init__(self, command = lambda: self.g.insertValue('8'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Nine(Button):
    def __init__(self, master):
        self.g = master
        self.n = 9
        Button.__init__(self, command = lambda: self.g.insertValue('9'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Zero(Button):
    def __init__(self, master):
        self.g = master
        self.n = 0
        Button.__init__(self, command = lambda: self.g.insertValue('0'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

class Add(Button):
    def __init__(self, master):
        self.g = master
        self.o = '+' #operand btns 
        Button.__init__(self, command = lambda: self.g.insertValue('+'), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o

class Subtract(Button):
    def __init__(self, master):
        self.g = master
        self.o = '-' #operand btns 
        Button.__init__(self, command = lambda: self.g.insertValue('-'), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o

class Multiply(Button):
    def __init__(self, master):
        self.g = master
        self.o = '*' #operand btns 
        Button.__init__(self, command = lambda: self.g.insertValue('*'), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o

class Divide(Button):
    def __init__(self, master):
        self.g = master
        self.o = '/' #operand btns 
        Button.__init__(self, command = lambda: self.g.insertValue('/'), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o
    
class Equal(Button):
    def __init__(self, master):
        self.g = master
        self.o = '=' #operand btns 
        Button.__init__(self, command = lambda: self.g.insertValue('='), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o

class Decimal(Button):
    def __init__(self, master):
        self.g = master
        self.o = '.' #operand btns 
        Button.__init__(self, command = lambda: self.g.insertValue('.'), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o

class Clear(Button):
    def __init__(self, master):
        self.g = master
        self.o = 'C' 
        Button.__init__(self, command = lambda: self.g.insertValue('C'), height = 3, width = 5, text = self.o)
    def value(self):
        return self.o
class Entry(Entry):
    def __init__(self, master):
        self.g = master
        self.o = '' 
        Button.__init__(self, command = lambda: self.g.insertValue('Entry'), height = 3, width = 13, text = self.o)
    def value(self):
        return self.o

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()





