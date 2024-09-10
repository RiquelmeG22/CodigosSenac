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

def login():
    usuario = usuarioentry.get()
    senha = senhaentry.get()
    
    if usuario == senha:
        messagebox.showerror("Erro","A senha não pode ser igual o usuário")
        return

    if senha != usuario:
        messagebox.showinfo("Sucesso","Cadastrado realizado com sucesso")
        return
 

root = tk.Tk()
root.title("Tela de Usuário")
root.geometry("300x450")
frm = tk.Frame(root, background='purple')
frm.pack(fill="both", padx=15, pady=15, expand=True)
root.resizable(False, False)

textologin =tk.Label(frm, text="Tela de Login", font=("Arial,",20), anchor="w")
textologin.place(rely=0.05, relx=0.5, anchor='n')

usuario = tk.Label(frm, text="Usuario", font=("Arial",15), anchor="w", justify="left")
usuario.place(rely=0.33, relx=0.22, anchor='n')
usuarioentry = tk.Entry(frm, font=("Arial",15))
usuarioentry.place(rely=0.47, relx=0.5, anchor='s')

senha = tk.Label(frm, text="Senha", font=("Arial",15), anchor="w", justify="left")
senha.place(rely=0.54, relx=0.20, anchor='n')
senhaentry = tk.Entry(frm, font=("Arial", 14), show='*')
senhaentry.place(rely=0.68, relx=0.5, anchor='s')

botaologin = tk.Button(frm, text="Login", font=("Arial",12), anchor="w", justify="center", command=login)
botaologin.place(rely=0.77, relx=0.7)
botaoregistar = tk.Button(frm, text='Registrar', font=("Arial", 12), anchor="w", justify="center")
botaoregistar.place(rely=0.77, relx=0.10)





root.mainloop()



