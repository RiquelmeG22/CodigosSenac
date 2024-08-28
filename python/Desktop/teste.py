
from tkinter import *
    
def querypg(text):
    print(text)
    
janela = Tk()
janela.title("query tools")
texto = Label(janela, text="insira seu código aqui")
texto.grid(column=0, row=0)
codigo = Entry(janela, width=100)
codigo.grid(column=0, row=1)
botao = Button(janela, text="Rodar código", command=lambda: querypg(codigo.get()))
botao.grid(column=0, row=2)
janela.mainloop()