import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#Tela inicial
def login():
    tLogin.tkraise()

def principal():
    tPrincipal.tkraise()

def tela():
    tela1.tkraise()

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
root.state('zoomed')


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



#TELA PRINCIPAL  ===             ==                     ==                  ==                 ==                 ==                    ==                    ==                    ==                                   


tPrincipal = tk.Frame(root, background='#yellow')

tPrincipal = tk.Frame(root, background='#ffff12')

tPrincipal.grid(column=0, row=0, sticky='nsew')

titulo1 = tk.Label(tPrincipal, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulo1.place(rely=0.00, relx=0.5, anchor='n')

## bebidas alcolicas

bebidaalcolica = Image.open("imagens\\balcol.png")
bebidaalcolica.thumbnail((300, 300))
photo1 = ImageTk.PhotoImage(bebidaalcolica)
label1 = tk.Label(tPrincipal, image=photo1, bg="gray", bd=0)
label1.place(rely=0.3, relx=0.5, anchor='s')
#label1.grid(column=1, row=1, pady=10)

botalcol = Image.open("imagens\\botbedalcolicas.png")
botalcol1 = ImageTk.PhotoImage(botalcol)
balcol = tk.Label(tPrincipal, image=botalcol1, bd=0)
balcol.place(rely=0.32, relx=0.5, anchor='n')
balcol.bind('<Button-1>', lambda e: print('Opa'))


## sobremesas


sobremesa = Image.open("imagens\\sobremesa2.jpg")
sobremesa.thumbnail((300, 300))
photo2 = ImageTk.PhotoImage(sobremesa)
label2 = tk.Label(tPrincipal, image=photo2, bg="gray", bd=0)
label2.place(rely=0.42, relx=0.5, anchor='n')


botsobremesa = Image.open("imagens\\bsobremesas.png")
botsobremesa1 = ImageTk.PhotoImage(botsobremesa)
botsobremesa = tk.Label(tPrincipal, image=botsobremesa1, bd=0)
botsobremesa.place(rely=0.63, relx=0.5, anchor='n')
botsobremesa.bind('<Button-1>', lambda e: print('Opa hehe'))

## pratos principais

pratoprincipal = Image.open("imagens\\pratoprincipal2.jpg")
pratoprincipal.thumbnail((300, 300))
photo3 = ImageTk.PhotoImage(pratoprincipal)
label3 = tk.Label(tPrincipal, image=photo3, bg="gray", bd=0)
label3.place(rely=0.42, relx=0.25, anchor='n')

botpratoprincipal = Image.open("imagens\\bpratoprincipais.png")
botpratoprincipal1 = ImageTk.PhotoImage(botpratoprincipal)
botpratoprincipal = tk.Label(tPrincipal, image=botpratoprincipal1, bd=0)
botpratoprincipal.place(rely=0.63, relx=0.25, anchor='n')
botpratoprincipal.bind('<Button-1>', lambda e: print('Opa hehe'))


## entradas

entradas = Image.open("imagens\\petiscos.jpg")
entradas.thumbnail((300, 300))
photo4 = ImageTk.PhotoImage(entradas)
label4 = tk.Label(tPrincipal, image=photo4, bg="gray", bd=0)
label4.place(rely=0.3, relx=0.25, anchor='s')

botentradas = Image.open("imagens\\bentradas.png")
botentradas1 = ImageTk.PhotoImage(botentradas)
botentradas = tk.Label(tPrincipal, image=botentradas1, bd=0)
botentradas.place(rely=0.32, relx=0.25, anchor='n')
botentradas.bind('<Button-1>', lambda e: print('Opa kkkkkkkkkk'))

## bebidas

bebidas = Image.open("imagens\\bebidas.jpg")
bebidas.thumbnail((300, 300))
photo5 = ImageTk.PhotoImage(bebidas)
label5 = tk.Label(tPrincipal, image=photo5, bg="gray", bd=0)
label5.place(rely=0.3, relx=0.75, anchor='s')

botbebidas = Image.open("imagens\\botaobebida.png")
botbebidas1 = ImageTk.PhotoImage(botbebidas)
botbebidas = tk.Label(tPrincipal, image=botbebidas1, bd=0)
botbebidas.place(rely=0.32, relx=0.75, anchor='n')
botbebidas.bind('<Button-1>', lambda e: tela())

## master chef

mastercehf = Image.open("imagens\\masterchef.png")
mastercehf.thumbnail((300, 300))
photo6 = ImageTk.PhotoImage(mastercehf)
label6 = tk.Label(tPrincipal, image=photo6, bg="gray", bd=0)
label6.place(rely=0.42, relx=0.75, anchor='n')

botmasterchef = Image.open("imagens\\botaomenuchef.png")
botmasterchef1 = ImageTk.PhotoImage(botmasterchef)
botmasterchef = tk.Label(tPrincipal, image=botmasterchef1, bd=0)
botmasterchef.place(rely=0.63, relx=0.75, anchor='n')
botmasterchef.bind('<Button-1>', lambda e: print('Opa kkkkkkkkkk'))



## TELA 1 ==                    ==                            ==                                 ==                                      ==                                ==


tela1 = tk.Frame(root, background='#ffff12')
tela1.grid(column=0, row=0, sticky='nsew')










login()
root.mainloop()
 