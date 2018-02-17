from tkinter import *

master = Tk()

def sel():
    print(w.get())

#w = Spinbox(master, from_=0, to=10)
w = Spinbox(master, values=(2, 4, 6 ,8), command=sel)
w.pack()

mainloop()
