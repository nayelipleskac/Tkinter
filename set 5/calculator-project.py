#set 6  
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd
from PIL import Image, ImageTk

root = Tk()
root.title('Calculator Project')

root.geometry('600x550')

#listbox w/ historybtn
#do the photo backspace 

class Calculator(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.numList = []
        self.operandsList = []
        self.history = []
        self.flag = 0


        self.keypadFrame = Frame(self, width = 10, height = 5, bg = 'red')
        self.entryFrame = Frame(self, height = 5, width = 10, bg = 'green')
        self.listboxFrame = Frame(self, width = 200, height = 150, bg= 'purple')
        self.clearbtn = Clear(self)
        self.entrybox = EntryLabel(self)
        # self.deletebtn = Delete(self)
        self.historybtn = History(self)

        self.btn1 = One(self)
        self.btn2 = Two(self) 
        self.btn3 = Three(self)
        self.btn4 = Four(self)
        self.btn5 = Five(self)
        self.btn6 = Six(self)
        self.btn7 = Seven(self)
        self.btn8 = Eight(self)
        self.btn9 = Nine(self)
        self.decimalbtn = Decimal(self)
        self.btn0 = Zero(self)
        self.equalbtn = Equal(self)

        self.addbtn = Add(self)
        self.subtractbtn = Subtract(self)
        self.multiplybtn = Multiply(self)
        self.dividebtn = Divide(self)

        # self.scrollbar= Scrollbar(self, orient = VERTICAL)
        self.listbox = ListboxFrame(self)
        self.scrollbar = ScrollBarFrame(self)


        # self.listbox_frame = Frame(root, width = 100, height= 200, bg = 'gray')
        # self.scrollbar = Scrollbar(self.listbox_frame, orient = VERTICAL)
        # self.listbox = Listbox(self.listbox_frame, yscrollcommand = self.scrollbar.set)

    def grid(self):
        self.entryFrame.grid(row = 0, column = 0)
        self.keypadFrame.grid(row = 1, column = 0)
        self.entrybox.grid(row = 0, column =1)

        self.historybtn.grid(row = 1, column = 0)
        # self.deletebtn.grid(row = 1, column = 1)
        self.clearbtn.grid(row = 1, column = 2)

        self.btn1.grid(row = 2, column = 0)
        self.btn2.grid(row = 2, column = 1)
        self.btn3.grid(row = 2, column = 2)

        self.btn4.grid(row = 3, column = 0)
        self.btn5.grid(row = 3, column = 1)
        self.btn6.grid(row = 3, column = 2)

        self.btn7.grid(row = 4, column = 0)
        self.btn8.grid(row = 4, column = 1)
        self.btn9.grid(row = 4, column = 2)

        self.decimalbtn.grid(row = 5, column = 0)
        self.btn0.grid(row = 5, column = 1)
        self.equalbtn.grid(row = 5, column = 2)

        self.addbtn.grid(row = 2, column = 3)
        self.subtractbtn.grid(row = 3, column = 3)
        self.multiplybtn.grid(row = 4, column = 3)
        self.dividebtn.grid(row = 5, column= 3)

        # self.listboxFrame.grid(row= 6, column = 0)

        

        # self.listbox.pack(side = RIGHT, fill = BOTH, expand = 1)
        # self.scrollbar.pack(side = RIGHT, fill = Y)


    def insertValue(self, target):
        self.t = None
        if target == '1':
            self.numList.append(str(self.btn1.value()))
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)
        if target == '2':
            self.numList.append(str(self.btn2.value()))
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)
        if target == '3':
            self.numList.append(str(self.btn3.value()))
            self.entrybox.insert(0,self.btn3.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '4':   
            self.numList.append(str(self.btn4.value()))
            self.entrybox.insert(0,self.btn4.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '5':
            self.numList.append(str(self.btn5.value()))
            self.entrybox.insert(0,self.btn5.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '6':
            self.numList.append(str(self.btn6.value()))
            self.entrybox.insert(0,self.btn6.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '7':
            self.numList.append(str(self.btn7.value()))
            self.entrybox.insert(0, self.btn7.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '8':
            self.numList.append(str(self.btn8.value()))
            self.entrybox.insert(0,self.btn8.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '9':
            self.numList.append(str(self.btn9.value()))
            self.entrybox.insert(0,self.btn9.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '0':
            self.numList.append(str(self.btn0.value()))
            self.entrybox.insert(0,self.btn0.n)
            self.entrybox.delete(0, END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        
        if target == '+':
            self.operandsList.append(self.addbtn.value())
            self.numList.append(self.addbtn.value())
            self.entrybox.delete(0,END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)
            

        if target == '-':
            self.operandsList.append(self.subtractbtn.value())
            self.numList.append(self.subtractbtn.value())
            self.entrybox.delete(0,END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '*':
            self.operandsList.append(self.multiplybtn.value())
            self.numList.append(self.multiplybtn.value())
            self.entrybox.delete(0,END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '/':
            self.operandsList.append(self.dividebtn.value())
            self.numList.append(self.dividebtn.value())
            self.entrybox.delete(0,END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == '=':
            self.operandsList.append(self.equalbtn.value())
            # self.numList.append(self.equalbtn.value())
            #calculate results
            # operand_index = self.numList(self.operandsList)
            
            expression = ''.join(self.numList)
            eval_expression = eval(expression)
            print(eval_expression)
            self.entrybox.delete(0,END)
            self.entrybox.insert(0, eval_expression)

            self.history.append(expression)

        if target == '.': 
            self.operandsList.append(self.decimalbtn.value())
            self.numList.append(self.decimalbtn.value())
            self.entrybox.delete(0,END)
            for nums in self.numList:
                self.entrybox.insert(END, nums)

        if target == 'C':
            #clear entry box
            self.entrybox.delete(0, END)
            self.numList.clear()
            print('user has cleared entry box')

        if target == 'History':
            self.flag+=1
            print('SELF.FLAG = ', self.flag)
            if  (self.flag %2) == 0:
                print('flag is even')
                self.listbox.grid_remove()
            else: 
                print('flag is odd')
                self.listbox.delete(0, END)
                for each in self.history:
                    self.listbox.insert(0,each)
                    print('hisory ', each)
                self.scrollbar.config(command = self.listbox.yview)
                self.listbox.grid(row = 6, column = 0, rowspan = 5)


        if target == 'Delete':
            self.numList.pop()
            self.entrybox.delete(0,END)
            self.entrybox.insert(0, self.numList)
            #delete the last digit of number in entry box
        self.debug()

  
    def debug(self):
        print('numList: ', self.numList)
        print('operands: ', self.operandsList)




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
        Button.__init__(self, command = lambda: self.g.insertValue('C'), height = 2, width = 5, text = self.o)
    def value(self):
        return self.o

class History(Button):
    def __init__(self, master):
        self.g = master
        self.o = 'History' 
        Button.__init__(self, command = lambda: self.g.insertValue('History'), height = 2, width = 15, text = self.o)
    def value(self):
        return self.o #num value list equations

class Delete(Button):
    def __init__(self, master):
        self.g = master
        img = Image.open(r'C:/Users/plesk/Downloads/delete.png') 
        resize_img = img.resize((50,50))
        resize_img = resize_img.save('C:/Users/plesk/Downloads/delete1.png')
        delete_img = ImageTk.PhotoImage(file = 'C:/Users/plesk/Downloads/delete1.png')

        img_label = Label(self, image = delete_img)
        img_label.grid(row = 1, column = 1)
        
            # img1 = Image.open('germany.png')
            # resize_img = img1.resize((100,50))
            # germany_img = ImageTk.PhotoImage(resize_img)
            # germany_flag_label = Label(frame1, image = germany_img)
            # germany_flag_label.pack()


        # self.img_png = 'delete!'
        self.o = 'Delete'
        Button.__init__(self, image = delete_img, command = lambda: self.g.insertValue('Delete'))
    def value(self):
        return self.o

class EntryLabel(Entry):
    def __init__(self, master):
        self.g = master
        self.o = ''
        Entry.__init__(self, text = self.o, font = ('Arial', 18))
    def value(self):
        return self.o

class ScrollBarFrame(Scrollbar):
    def __init__(self, master):
        self.g = master
        self.o = 'Scrollbar'
        Scrollbar.__init__(self, orient = VERTICAL)
    def value(self):
        return self.o

class ListboxFrame(Listbox):
    def __init__(self, master):
        self.g = master
        self.o = 'Listbox'
        self.scrollbar = ScrollBarFrame(self)
        Listbox.__init__(self, yscrollcommand = self.scrollbar.set, font = ('Arial', 12))
    def value(self):
        return self.o




if __name__ == '__main__':
    app = Calculator()
    app.grid()
    app.mainloop()





