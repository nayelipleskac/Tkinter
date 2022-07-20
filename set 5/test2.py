import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.label = tk.Label(text = 'Hello World ')
        self.label.pack(padx = 10, pady = 10)
        tk.__init__(self)
        self.run()
    def run(self):
        pass
        # self.grid()
        # self.timelabel.start()
    

app = SampleApp()
app.mainloop()

##

