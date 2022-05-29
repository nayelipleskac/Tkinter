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
        
        self.btn1 = One(self)
        self.btn1.grid(row = 0, column = 0)
        self.btn2 = Two(self)
        self.btn2.grid(row = 0, column = 1)
    def insertValue(self, target):
        self.t = None
        if target == '1':
            self.numList.append(self.btn1.value())
        self.debug()
        if target == '2':
            self.numList.append(self.btn2.value())
        self.debug()
    def debug(self):
        print('numList: ', self.numList)

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



