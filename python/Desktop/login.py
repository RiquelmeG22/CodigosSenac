import tkinter as tk 
from tkinter import messagebox
import mysql.connector as sql


import tkinter as tk 
from tkinter import messagebox
db = sql.connect (host= '10.28.2.71',
                  user= 'suporte',
                  password = 'suporte',
                  db = 'login')

cursor = db.cursor() 

cursor.execute(f'select * from cadastro')
oi = cursor.fetchall()
print(oi)

def exibirtela(tela):
    try:
        tela.tkraise()
    except Exception:
        print("Erro!!")
        return
    
def telalogin():
    if(frm.winfo_children()):
        exibirtela(frm)
        return
    
    textologin =tk.Label(frm, text="Tela de Login", font=("Arial,",20), anchor="w")
    textologin.place(rely=0.05, relx=0.5, anchor='n')

    usuario = tk.Label(frm, text="Usuario", font=("Arial",15), anchor="w", justify="left")
    usuario.place(rely=0.33, relx=0.30, anchor='n')
    usuarioentry = tk.Entry(frm, font=("Arial",15))
    usuarioentry.place(rely=0.45, relx=0.5, anchor='s')

    senha = tk.Label(frm, text="Senha", font=("Arial",15), anchor="w", justify="left")
    senha.place(rely=0.51, relx=0.30, anchor='n')
    senhaentry = tk.Entry(frm, font=("Arial", 14), show='*')
    senhaentry.place(rely=0.63, relx=0.5, anchor='s')

    botaologin = tk.Button(frm, text="Login", font=("Arial",12), anchor="w", justify="center", command=lambda: login(usuarioentry, senhaentry))
    botaologin.place(rely=0.77, relx=0.7)
    botaoregistar = tk.Button(frm, text='Cadastro', font=("Arial", 12), anchor="w", justify="center", command=cadastro)
    botaoregistar.place(rely=0.77, relx=0.10)

    exibirtela(frm)

def cadastro():
    if(tela2.winfo_children()):
        exibirtela(tela2)
        return
    

    telacadastro =tk.Label(tela2, text="Tela de Cadastro", font=("Arial,",20), anchor="w")
    telacadastro.place(rely=0.05, relx=0.37, anchor='n')


    cadastro1 = tk.Label(tela2, text="Usuario", font=("Arial",15), anchor="w", justify="left")
    cadastro1.place(rely=0.20, relx=0.22, anchor='n')
    cadstroentry = tk.Entry(tela2, font=("Arial",15))
    cadstroentry.place(rely=0.32, relx=0.40, anchor='s')

    senhacadastro = tk.Label(tela2, text="Senha", font=("Arial",15), anchor="w", justify="left")
    senhacadastro.place(rely=0.35, relx=0.20, anchor='n')
    senhacadentry = tk.Entry(tela2, font=("Arial", 14), show='*')
    senhacadentry.place(rely=0.47, relx=0.40, anchor='s')

    confirmcadastro = tk.Label(tela2, text="Confirmação de senha", font=("Arial",15), anchor="w", justify="left")
    confirmcadastro.place(rely=0.50, relx=0.37, anchor='n')
    confsenhacadentry = tk.Entry(tela2, font=("Arial", 14), show='*')
    confsenhacadentry.place(rely=0.62, relx=0.40, anchor='s')

    textocadastro = tk.Label(tela2, text="Texto", font=("Arial",15), anchor="w", justify="left")
    textocadastro.place(rely=0.65, relx=0.20, anchor='n')
    textentry = tk.Entry(tela2, font=("Arial", 14))
    textentry.place(rely=0.77, relx=0.40, anchor='s')


    botaocadastar = tk.Button(tela2, text="Cadastrar", font=("Arial",12), anchor="w", justify="center", command=telalogin)
    botaocadastar.place(rely=0.83, relx=0.5)

    exibirtela(tela2)

def login(user, password):
    usuario = user.get()
    senha = password.get()
    
    cursor.execute(f'select usuario from cadastro where usuario="{usuario}" ')

    tcadastro = cursor.fetchone()
    print(tcadastro)
    if not tcadastro:
        messagebox.showerror("Erro","Usuario não existe")
        return

    cursor.execute(f'select senha from cadastro where usuario="{usuario}" ')
    testesenha = cursor.fetchone()
    print(testesenha[0])

    if senha != testesenha[0]:
        messagebox.showinfo("Erro","A sua senha está incorreta, por favor digite novamente!!")
        return
 

root = tk.Tk()
root.title("Tela de Usuário")
root.geometry("400x550")
root.resizable(False, False)

## tela login
frm = tk.Frame(root, background='purple')
frm.place(relheight=1, relwidth=1)

## tela cadastro
tela2 = tk.Frame(root, background='yellow')
tela2.place(relheight=1, relwidth=1)

telalogin()
root.mainloop()








    


  




