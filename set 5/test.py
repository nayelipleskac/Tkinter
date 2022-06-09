from tkinter import *
from tkinter import messagebox

from tkinter import filedialog as fd

root = Tk()
root.title('Calculator Project')

root.geometry('500x400')

numlist = ['0','2']
print(numlist.index('2'))

entry = Entry(root, text = numlist)
entry.pack()



root.mainloop()