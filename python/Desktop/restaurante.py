import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox








#Tela inicial
def login():
    tLogin.tkraise()

def principal():
    tPrincipal.tkraise()

def validarLogin():
    usuario = usuarioentry.get()
    senha = senhaentry.get()
    confimsenha = confirmsenha.get()
    #if  usuario == '' or usuario == senha:
    #    messagebox.showerror("ERRO","A senha não pode ser igual o usuário.")
    #    return
    #elif senha != confimsenha:
    #    messagebox.showerror("ERRO","A senha que você digitou não está igual a de cima.")
    #    return
 
    principal()


 
#Tela de login
root = tk.Tk()
root.title("Restaurante")
root.geometry("800x800")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


tLogin = tk.Frame(root, background='white')
tLogin.columnconfigure(0, weight=2)
tLogin.columnconfigure(1, weight=1)
tLogin.columnconfigure(2, weight=2)
tLogin.grid(column=0, row=0, sticky='nsew')

titulo = tk.Label(tLogin, text="Restaurante do Ederson", anchor="center")
titulo.grid(column=1, row=0, sticky="we")
titulo.config(font=("Arial", 15, "bold"))
 
 
usuario = tk.Label(tLogin, text="Usuario ", font=("Arial",15), anchor="w", justify="left")        
usuario.grid(column=1, row=1, sticky="we", pady=(15,0))

usuarioentry = tk.Entry(tLogin, font=("Arial",14))
usuarioentry.grid(column=1, row=2, sticky="we")
 
senha = tk.Label(tLogin, text="Senha", font=("Arial",15), anchor="w", justify="left")        
senha.grid(column=1, row=3, sticky="we", pady=(15,0))

senhaentry = tk.Entry(tLogin, font=("Arial",14), show="*")
senhaentry.grid(column=1, row=4, sticky="we")
 
confirmsenha = tk.Label(tLogin, text="Confirmação de senha", font=("Arial",15), anchor="w", justify="left")    
confirmsenha.grid(column=1, row=5, sticky="we", pady=(15,0))

confirmsenha = tk.Entry(tLogin, font=("Arial",14), show="*")
confirmsenha.grid(column=1, row=6, sticky="we")
 
botao = tk.Button(tLogin, text="Cadastrar", font=("Arial",15), anchor="w", justify="left", command=validarLogin)
botao.grid(column=1, row=7, pady=20)  



#TELA 1 ===             ==                     ==                  ==                 ==                 ==                    ==                    ==                    ==                                   

tPrincipal = tk.Frame(root, background='#FFFFFF')
tPrincipal.columnconfigure(0, weight=2)
tPrincipal.columnconfigure(1, weight=1)
tPrincipal.columnconfigure(2, weight=2)
tPrincipal.columnconfigure(3, weight=2)
tPrincipal.columnconfigure(4, weight=2)


tPrincipal.grid(column=0, row=0, sticky='nsew')


titulo1 = tk.Label(tPrincipal, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulo1.grid(column=2, row=0, sticky="we", pady=50)

bebidaalcolica = Image.open("imagens\\balcol.png")
bebidaalcolica.thumbnail((300, 300))
photo1 = ImageTk.PhotoImage(bebidaalcolica)



botalcol = Image.open("imagens\\bentrada.png")
botalcol1 = ImageTk.PhotoImage(botalcol)

oi = tk.Label(tPrincipal, image=botalcol1, bd=0)
oi.grid (column=1, row= 3)
oi.bind('<Button-1>', lambda e: print('Opa'))



label1 = tk.Label(tPrincipal, image=photo1, bg="gray", bd=0)
label1.grid(column=1, row=1, pady=10)

sobremesa = Image.open("imagens\\sobremesa2.jpg")
sobremesa.thumbnail((300, 300))
photo2 = ImageTk.PhotoImage(sobremesa)

oi = ("print")
label2 = tk.Label(tPrincipal, image=photo2, bg="gray", bd=0)
label2.grid(column=3, row=1, pady=10)


pratoprincipal = Image.open("imagens\\pratoprincipal2.jpg")
pratoprincipal.thumbnail((300, 300))
photo3 = ImageTk.PhotoImage(pratoprincipal)


label3 = tk.Label(tPrincipal, image=photo3, bg="gray", bd=0)
label3.grid(column=2, row=1, pady=10)


petiscos = Image.open("imagens\\petiscos.jpg")
petiscos.thumbnail((300, 300))
photo4 = ImageTk.PhotoImage(petiscos)


label4 = tk.Label(tPrincipal, image=photo4, bg="gray", bd=0)
label4.grid(column=3, row=2, pady=150)


bebidas = Image.open("imagens\\bebidas.jpg")
bebidas.thumbnail((300, 300))
photo5 = ImageTk.PhotoImage(bebidas)


label5 = tk.Label(tPrincipal, image=photo5, bg="gray", bd=0)
label5.grid(column=2, row=2, pady=15)


mastercehf = Image.open("imagens\\masterchef.png")
mastercehf.thumbnail((300, 300))
photo6 = ImageTk.PhotoImage(mastercehf)


label6 = tk.Label(tPrincipal, image=photo6, bg="gray", bd=0)
label6.grid(column=1, row=2, pady=15)


login()
root.mainloop()
 