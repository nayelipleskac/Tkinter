#set 6  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd

root = Tk()
root.title('Calculator Project')

root.geometry('400x400')

class Custom_button:
    def __init__(self):
        
        # self.button = Button(root, text = num)
        self.name = ['1','2','3','4','5','6','7','8','9']
        self.row_number = 0
        self.column_number = 0
    def draw_button(self):
        for name in range(0,10,1):
            for row in range(0, 3, 1):
                for column in range(0,3,1):
                    # for num in range(0,10,1):
                    num=row+column
                    print('row ', row, 'column ', column, 'num ', name)
                    button = Button(root, text = name, height = 3, width=5)  
                    button.grid(row = row, column = column)


buttonUI = Custom_button()
buttonUI.draw_button()
root.mainloop()