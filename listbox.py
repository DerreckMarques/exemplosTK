from tkinter import *

def sel():
    print(lb1.curselection())

top = Tk()

lb1 = Listbox(top)
lb1.insert(1, "Python")
lb1.insert(2, "Perl")
lb1.insert(3, "C")
lb1.insert(4, "PHP")
lb1.insert(5, "JSP")
lb1.insert(6, "Ruby")

b1 = Button(top, text="pesquisa", command=sel)


lb1.pack()
b1.pack()

top.mainloop()
