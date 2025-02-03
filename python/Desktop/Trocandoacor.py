

import tkinter as tk



def arcoiris(color):
    root.configure(bg=color)


root = tk.Tk()
root.title("Trocar a cor de fundo")
root.geometry("300x200")  
root.resizable(width=False, height=False)


botaovermelho = tk.Button(root, text="Vermelho", font=('Arial',13), command=lambda: arcoiris("red"))
botaovermelho.pack(pady=10)

botaoverde = tk.Button(root, text="Verde", font=('Arial',13), command=lambda: arcoiris("green"))
botaoverde.pack(pady=10)

botaoazul = tk.Button(root, text="Azul", font=('Arial',13), command=lambda: arcoiris("blue"))
botaoazul.pack(pady=10)


root.mainloop()

