from tkinter import *

root = Tk()

def hello():
    print('Hello')

#create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=root.quit)

#display the menu
root.config(menu=menubar)
