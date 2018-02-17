from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a labelFrame")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

label = Label(labelframe, text="testando labelframe")
label.pack()

root.geometry("500x500")
mainloop()
