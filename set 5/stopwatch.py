# # Python program to illustrate a stop watch
# # using Tkinter
# #importing the required libraries
# import tkinter as Tkinter
# from datetime import datetime
# counter = 66600
# running = False
# def counter_label(label):
#     def count():
#         if running:
#             global counter
   
#             # To manage the initial delay.
#             if counter==66600:            
#                 display="Starting..."
#             else:
#                 tt = datetime.fromtimestamp(counter)
#                 string = tt.strftime("%H:%M:%S")
#                 display=string
   
#             label['text']=display   # Or label.config(text=display)
   
#             # label.after(arg1, arg2) delays by 
#             # first argument given in milliseconds
#             # and then calls the function given as second argument.
#             # Generally like here we need to call the 
#             # function in which it is present repeatedly.
#             # Delays by 1000ms=1 seconds and call count again.
#             label.after(1000, count) 
#             counter += 1
   
#     # Triggering the start of the counter.
#     count()     
   
# # start function of the stopwatch
# def Start(label):
#     global running
#     running=True
#     counter_label(label)
#     start['state']='disabled'
#     stop['state']='normal'
#     reset['state']='normal'
   
# # Stop function of the stopwatch
# def Stop():
#     global running
#     start['state']='normal'
#     stop['state']='disabled'
#     reset['state']='normal'
#     running = False
   
# # Reset function of the stopwatch
# def Reset(label):
#     global counter
#     counter=66600
   
#     # If rest is pressed after pressing stop.
#     if running==False:      
#         reset['state']='disabled'
#         label['text']='Welcome!'
   
#     # If reset is pressed while the stopwatch is running.
#     else:               
#         label['text']='Starting...'
   
# root = Tkinter.Tk()
# root.title("Stopwatch")
   
# # Fixing the window size.
# root.minsize(width=250, height=70)
# label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
# label.pack()
# f = Tkinter.Frame(root)
# start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
# stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
# reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
# f.pack(anchor = 'center',pady=5)
# start.pack(side="left")
# stop.pack(side ="left")
# reset.pack(side="left")
# root.mainloop()



import tkinter as tink
count = -1
run = False
def var_name(mark):
   def value():
      if run:
         global count
         # Just beore starting
         if count == -1:
            show = "Starting"
         else:
            show = str(count)
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value)
         count += 1
   value()
# While Running
def Start(mark):
   global run
   run = True
   var_name(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'
# While stopped
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False
# For Reset
def Reset(label):
   global count
   count = -1
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Welcome'
   else:
      mark['text'] = 'Start'

base = tink.Tk()
base.title("PYTHON STOPWATCH")
base.minsize(width=300, height=200)
mark = tink.Label(base, text="Welcome", fg="blue", font="Times 25 bold",bg="white")
mark.pack()
start = tink.Button(base, text='Start',width=25, command=lambda: Start(mark))
stop = tink.Button(base, text='Stop', width=25, state='disabled', command=Stop)
reset = tink.Button(base, text='Reset',width=25, state='disabled', command=lambda: Reset(mark))
start.pack()
stop.pack()
reset.pack()
base.mainloop()
