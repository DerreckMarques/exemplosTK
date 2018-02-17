from tkinter import *

def bt_click():
    #print(ed.get())
    lb["text"] = ed.get()
    
janela = Tk()

ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text="OK", command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text="Label")
lb.place(x=100, y=200)

janela.geometry("300x300")
janela.mainloop()






  '''s.send(arquivo.encode())
            #dados = s.recv(1024).decode()
            
            file = open('te.txt', 'w')

            with file:
                while True:
                    print('escrevendo dados.')
                    dados = s.recv(1024).decode()
                    if not dados: break
                    print(dados)
                    
        
                    file.writelines(dados)
            '''
