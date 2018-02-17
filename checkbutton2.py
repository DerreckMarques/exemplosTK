#https://desenvolvimentoaberto.org/2014/03/13/visual-controles-checkbutton-check-status-text-line-continue-onclick-python-linux/
from tkinter import *
#cria formulario
formulario = Tk()
formulario.title = "Desenvolvimento Aberto"
#evento CB on click
def evento1():
    if(c1.get() == 1):
        texto.insert(END, "Voce selecionou no checkbox1\n")
    else:
        texto.insert(END, "Voce deselecionou no checkbox1\n")

def evento2():
    if(c2.get() == 1):
        texto.insert(END, "Voce selecionou no checkbox2\n")
    else:
        texto.insert(END, "Voce deselecionou no checkbox2\n")


def evento3():
    if(c1.get() == 1):
        texto.insert(END, "Voce selecionou no checkbox3\n")
    else:
        texto.insert(END, "Voce deselecionou no checkbox3\n")

#cria variavel para status do checkbox
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
#cria um novo label
rotulo = Label(formulario, text="Concatena Strings")
#criação do Checkbutton
opc1 = Checkbutton(formulario, text="Opcao1", \
                    variable=c1, \
                   command = evento1)

opc2 = Checkbutton(formulario, text="Opcao2", \
                    variable=c2, \
                   command = evento2)

opc3 = Checkbutton(formulario, text="Opcao3", \
                    variable=c3, \
                   command = evento3)

texto = Text(formulario, height=10, width=50)
#adiciona componentes no Grid
rotulo.grid(row=0, column=1)
opc1.grid(row=1, column=1)
opc2.grid(row=2, column=1)
opc3.grid(row=3, column=1)
texto.grid(row=4, column=1)
#Roda o loop principal
mainloop()





