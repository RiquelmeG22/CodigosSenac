
import tkinter as tk 
from tkinter import messagebox


def cadastrar():
    usuario = usuarioentry.get()
    senha = senhaentry.get()
    confisenha = confrsenhaentry.get()
    

    if usuario == senha:
        messagebox.showerror("Erro","A senha não pode ser igual o usuário")
        return

    if senha == confisenha:
        messagebox.showinfo("Sucesso","Cadastrado realizado com sucesso")
        return
    else:
        messagebox.showerror("Erro","A senha que voce digitou não esta igual")
        return


root = tk.Tk()
root.title("Tela de Usuário")
root.geometry("250x250")
frm = tk.Frame(root)
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.columnconfigure(2, weight=1)

usuario = tk.Label(frm, text="Usuario", font=("Arial",15), anchor="w", justify="left")
usuario.grid(column=1, row=0, sticky="we")
frm.pack(fill="x", padx=15, pady=15)
senha = tk.Label(frm, text="Senha", font=("Arial",15), anchor="w", justify="left")
senha.grid(column=1, row=2, sticky="we")
usuarioentry = tk.Entry(frm, font=("Arial",14))
usuarioentry.grid(column=1, row=1)
confirsenha = tk.Label(frm, text="Confirmação de senha", font=("Arial",15), anchor="w", justify="left")
confirsenha.grid(column=1, row=4, sticky="we")
confrsenhaentry = tk.Entry(frm, font=("Arial",14))
confrsenhaentry.grid(column=1, row=5)
senhaentry = tk.Entry(frm, font=("Arial", 14))
senhaentry.grid(column=1, row=3)

botao = tk.Button(frm, text="Cadastrar", font=("Arial",15), anchor="w", justify="left", command=cadastrar)
botao.grid(column=1, row=6)



root.mainloop()



