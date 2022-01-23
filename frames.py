import tkinter as tk
import pygame 
pygame.init()
from tkinter import Button, Entry, Frame, Image, Label, PhotoImage, StringVar, IntVar, messagebox
from tkinter.constants import END, LEFT, RIGHT, TOP
from PIL import Image,ImageTk
root =  tk.Tk()

root.title('Flags')

root.geometry('180x200')
#1
# vertical_frame1 = Frame(root,width = 60, height = 200, bg = 'blue')
# vertical_frame1.pack(side = LEFT)

# vertical_frame2 = Frame(root,width =60, height = 200, bg = 'red')
# vertical_frame2.pack(side= RIGHT)

# horizontal_frame = Frame(root, width =150, height = 50, bg = 'red')
# horizontal_frame.pack()

#2
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Flags')

def placeFrames():
    frame1 = Frame(root, width = 100, height = 50)
    frame1.grid(row = 1, column = 1)
    label1 = Label(root, text = 'Germany')
    label1.pack(side = TOP)
    frame2 = Frame(root, width = 100, height = 50)
    frame2.grid(row = 1, column = 2)
    label2 = Label(root, text = 'Greece')
    label2.pack(side = TOP)

    frame3 = Frame(root, width = 100, height = 50)
    frame3.grid(row = 2, column = 1)
    label3 = Label(root, text = 'Italy')
    label3.pack(side = TOP)
    frame4 = Frame(root, width = 100, height = 50)
    frame4.grid(row = 2, column = 2)
    label4 = Label(root, text = 'US')
    label4.pack(side = TOP)

    # img1 = PhotoImage(file = 'germany.png')
    # germany_flag_label = Label(frame1, image = img1).pack()

def resize():
    # frame1 = Frame(root, width = 100, height = 100)
    # frame1.grid(row = 1, column = 1)
    # img1 = Image.open('germany.png')
    # resize_img = img1.resize((100,50))
    # germany_img = ImageTk.PhotoImage(resize_img)
    # germany_flag_label = Label(frame1, image = germany_img)
    # germany_flag_label.pack()

    frame2 = Frame(root, width = 100, height = 100)
    frame2.grid(row = 1, column = 2)
    img2 = Image.open('italy.png')
    resize_img = img2.resize((100,50))
    italy_img = ImageTk.PhotoImage(resize_img)
    italy_flag_label = Label(frame2, image = italy_img)
    italy_flag_label.pack()

white = (255,255,255)


# img = pygame.image.load('germany.png')

while True: 
    resize()

    root.update()


# render = ImageTk.PhotoImage(load)



# root.mainloop()
