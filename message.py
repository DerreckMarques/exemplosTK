from tkinter import *
from tkinter import messagebox

def hello():
    #messagebox.showinfo("Say hello", "Hello world")
    #messagebox.showwarning("Select User","Select a user to whisper to!")
    #messagebox.showerror("Error", "pagina nao configurada")
    #var = messagebox.askquestion("sobre o app", "Esta sendo util")
    #print(var)
    #var = messagebox.askokcancel("continuar", "tem certeza")
    #print(var)
    #var = messagebox.askyesno("tem certeza", "tem certeza")
    #print(var)
    messagebox.askretrycancel()

    
top = Tk()

b1 = Button(top, text="Say Hello", command=hello)
b1.pack()

top.geometry("300x300")
mainloop()
