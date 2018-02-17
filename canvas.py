from tkinter import *


top = Tk()

c = Canvas(top, bg="blue", height=250, width=300)

#codigo para fazer um arco no canvas
coord = 10, 50, 240, 210
arc = c.create_arc(coord, start=0, extent=150, fill="red")

#codigo para colocar uma imagem
filename = PhotoImage(file = "images.png")
image = c.create_image(150, 100, image=filename)

#codigo para criar uma linha
line = c.create_line(5, 50, 100, 150)

#criar circulo
oval = c.create_oval(5, 50, 100, 150)

c.pack()
top.mainloop()
