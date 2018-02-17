from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack(side=LEFT)

E1 = Entry(top, bd=5, bg="red")
E1.pack(side=RIGHT)
E1.delete(0, END)
E1.insert(0, "Digite seu nome aqui")
print(E1.get())

var = StringVar()
E2 = Entry(top, textvariable=var, bd=5, show="*")
E2.pack(side=RIGHT)

var.set("testando")
print(var.get())


top.mainloop()
