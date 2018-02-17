import tkinter as tk

janela = tk.Tk()
janela.title("aprendendo Tkinter")

janela["bg"] = "green"

#LarguraXAltura+(distancia da Esq)+(distancia do topo)
janela.geometry("800x300+100+100")

janela.mainloop()
