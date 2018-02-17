from tkinter import *


def processar():
    if(checkVar1 == 1 & checkVar2 == 1):
        messagebox.showinfo("vc escolheu musica e video")
        print(checkVar1)

top = Tk()

checkVar1 = 0
checkVar2 = 0

C1 = Checkbutton(top, text="Music", variable=checkVar1,
                 onvalue=1, offvalue=0, height=5, width=20)

C2 = Checkbutton(top, text="Video", variable=checkVar2,
                 onvalue=1, offvalue=0, height=5, width=20)

b = Button(top, text="continuar", command=processar)

C1.pack()
C2.pack()
b.pack()

top.mainloop()
