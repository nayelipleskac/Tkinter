#set 6  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd

root = Tk()
root.title('Calculator Project')

root.geometry('400x400')


class Calculator(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.numList = []

        self.output_screen = OutputScreen(self)
        # self.output_screen.grid(row  = 0, column = 0)

        self.btn1 = One(self)
        self.btn1.grid(row = 0, column = 0)
        self.btn2 = Two(self)
        self.btn2.grid(row = 0, column = 1)
        self.btn3 = Three(self)
        self.btn3.grid(row = 0, column = 2)
        self.btn4 = Four(self)
        self.btn4.grid(row = 1, column = 0)
        self.btn5 = Five(self)
        self.btn5.grid(row = 1, column = 1)
        self.btn6 = Six(self)
        self.btn6.grid(row = 1, column = 2)
        self.btn7 = Seven(self)
        self.btn7.grid(row = 2, column = 0)
        self.btn8 = Eight(self)
        self.btn8.grid(row = 2, column = 1)
        self.btn9 = Nine(self)
        self.btn9.grid(row = 2, column =2)

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
        self.debug()
  
    def debug(self):
        print('numList: ', self.numList)

class OutputScreen(Text):
    def __init__(self, master):
        self.g = master
        Text.__init__(self, height = 3, width = 25)


class One(Button):
    def __init__(self, master):
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

class Ten(Button):
    def __init__(self, master):
        self.g = master
        self.n = 10
        Button.__init__(self, command = lambda: self.g.insertValue('10'), height= 3, width = 5, text = self.n)
    def value(self):
        return self.n

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()




# class Custom_button:
#     def __init__(self):
        
#         # self.button = Button(root, text = num)
#         self.name = ['1','2','3','4','5','6','7','8','9']
#         self.row_number = 0
#         self.column_number = 0
#     def draw_button(self):
#         for name in range(0,10,1):
#             for row in range(0, 3, 1):
#                 for column in range(0,3,1):
#                     # for num in range(0,10,1):
#                     # num=row+column
#                     print('row ', row, 'column ', column, 'num ', name)
#                     button = Button(root, text = name, height = 3, width=5)  
#                     button.grid(row = row, column = column)


# buttonUI = Custom_button()
# buttonUI.draw_button()



