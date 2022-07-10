from tkinter import *
from tkinter import messagebox
import random

from tkinter import filedialog as fd

# root = Tk()
# root.title('Calculator Project')

# root.geometry('500x400')

# numlist = ['0','2']
# print(numlist.index('2'))

# entry = Entry(root, text = numlist)
# entry.pack()

# root.mainloop()


# imgDict = {1: 'img1', 2: 'img2', 3: 'img3', 4: 'img4', 5: 'img5'}
# print(imgDict[1])

class Test:
    def __init__(self):
        self.id = random.randint(1,10)
    
obj1 = Test()
obj2 = Test()

#find the name of the obj of whatever button the user pressed

print('obj1 id: ',obj1.id)
print('obj2 id: ',obj2.id)
