from tkinter import *

def bt_click():
    if(str(ed.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed.get())
        num2 = int(ed2.get())
        lb["text"] = num1+num2
    else:
        lb["text"] = "valores informados invalidos"

janela = Tk()

ed = Entry(janela)
ed.place(x=100, y=100)

ed2 = Entry(janela)
ed2.place(x=100, y=120)

bt = Button(janela, text="SOMA", width=20, command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text="")
lb.place(x=100, y=180)

janela.geometry("300x300")
janela.mainloop()
