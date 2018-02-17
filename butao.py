from tkinter import *

top = Tk()

def hello():
    messagebox.showinfo("Hello Python", "Hello World")
    

b = Button(top, text="hello", command=hello)
b.pack()

top.mainloop()
