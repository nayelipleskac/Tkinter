# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a Listbox widget
lb = Listbox(win, width=100, height=10, font=('Times 13'), selectbackground="black")
lb.pack()

# Define a function to edit the listbox ite
def save():
   for item in lb.curselection():
      print("You have selected " + str(item+1))

# Add items in the Listbox
lb.insert("end", "A", "B", "C", "D", "E", "F")

# Add a Button To Edit and Delete the Listbox Item
Button(win, text="Save", command=save).pack()

win.mainloop()