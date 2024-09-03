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

def telatwo():
    telat2.tkraise()

def telathree():
    telat3.tkraise()

def telafour():
    telat4.tkraise()

def telafive():
    telat5.tkraise()

def telasix():
    telat6.tkraise()

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


tPrincipal = tk.Frame(root, background='yellow')

# tPrincipal = tk.Frame(root, background='#ffff12')

tPrincipal.grid(column=0, row=0, sticky='nsew')

titulo1 = tk.Label(tPrincipal, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulo1.place(rely=0.00, relx=0.5, anchor='n')

## bebidas alcolicas

bebidaalcolica = Image.open("imagens\\balcol.png")
bebidaalcolica.thumbnail((300, 300))
photo1 = ImageTk.PhotoImage(bebidaalcolica)
label1 = tk.Label(tPrincipal, image=photo1, bg="gray", bd=0)
label1.place(rely=0.3, relx=0.5, anchor='s')


botalcol = Image.open("imagens\\botbedalcolicas.png")
botalcol1 = ImageTk.PhotoImage(botalcol)
balcol = tk.Label(tPrincipal, image=botalcol1, bd=0)
balcol.place(rely=0.32, relx=0.5, anchor='n')
balcol.bind('<Button-1>', lambda e: telathree())


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
botsobremesa.bind('<Button-1>', lambda e: telafive())

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
botpratoprincipal.bind('<Button-1>', lambda e: telafour())

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
botentradas.bind('<Button-1>', lambda e: telatwo())

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
botmasterchef.bind('<Button-1>', lambda e: telasix())

## TELA 1 ==                    ==                            ==                                 ==                                      ==                                ==

tela1 = tk.Frame(root, background='#ffff12')
tela1.grid(column=0, row=0, sticky='nsew')

titulo2 = tk.Label(tela1, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulo2.place(rely=0.00, relx=0.5, anchor='n')

## coca-cola           ==              ==              ==             ==             ==             ==

cocacola = Image.open("imagens\\bebidas\\CocaCola.png")
cocacola.thumbnail((300, 300))
foto1 = ImageTk.PhotoImage(cocacola)
lab1 = tk.Label(tela1, image=foto1, bg="gray", bd=0)
lab1.place(rely=0.3, relx=0.5, anchor='s')

botaococacola = Image.open("imagens\\bebidas\\botcoca.png")
botaococacola1 = ImageTk.PhotoImage(botaococacola)
botaococacola = tk.Label(tela1, image=botaococacola1, bd=0)
botaococacola.place(rely=0.32, relx=0.5, anchor='n')
botaococacola.bind('<Button-1>', lambda e: print('Opa'))


## aguacoco ==               ==                  ==                   ==               ==            ==

aguacoco = Image.open("imagens\\bebidas\\AguaCoco.png")
aguacoco.thumbnail((300, 300))
foto2 = ImageTk.PhotoImage(aguacoco)
lab2 = tk.Label(tela1, image=foto2, bg="gray", bd=0)
lab2.place(rely=0.52, relx=0.65, anchor='n')

botaoaguacoco = Image.open("imagens\\bebidas\\botaguacoco.png")
botaoaguacoco1 = ImageTk.PhotoImage(botaoaguacoco)
botaoaguacoco = tk.Label(tela1, image=botaoaguacoco1, bd=0)
botaoaguacoco.place(rely=0.81, relx=0.65, anchor="s")
botaoaguacoco.bind('<Button-1>', lambda e: print('Opa'))

 ## red-bull ==                    ==                ==                   ==                ==          ==

redbul = Image.open("imagens\\bebidas\\Red Bull.png")
redbul.thumbnail((300, 300))
foto3 = ImageTk.PhotoImage(redbul)
lab3 = tk.Label(tela1, image=foto3, bg="gray", bd=0)
lab3.place(rely=0.52, relx=0.35, anchor='n')

botaoredbull = Image.open("imagens\\bebidas\\botredbull.png")
botaoredbull1 = ImageTk.PhotoImage(botaoredbull)
botaoredbull = tk.Label(tela1, image=botaoredbull1, bd=0)
botaoredbull.place(rely=0.81, relx=0.35, anchor="s")
botaoredbull.bind('<Button-1>', lambda e: print('Opa'))

## suco de goiaba ==         ==                   ==                    ==                    ==

sucogoiaba = Image.open("imagens\\bebidas\\sucogoiaba22.png")
sucogoiaba.thumbnail((300, 300))
foto4 = ImageTk.PhotoImage(sucogoiaba)
lab4 = tk.Label(tela1, image=foto4, bg="gray", bd=0)
lab4.place(rely=0.3, relx=0.25, anchor='s')

botaosucogoiaba = Image.open("imagens\\bebidas\\botsucogoiaba.png")
botaosucogoiaba1 = ImageTk.PhotoImage(botaosucogoiaba)
botaosucogoiaba = tk.Label(tela1, image=botaosucogoiaba1, bd=0)
botaosucogoiaba.place(rely=0.32, relx=0.25, anchor='n')
botaosucogoiaba.bind('<Button-1>', lambda e: print('Opa'))


# suco de laranja ==         ===                   ==             ==               ==         ==    

sucolaranja = Image.open("imagens\\bebidas\\sucolaranja22.png")
sucolaranja.thumbnail((300, 300))
foto5 = ImageTk.PhotoImage(sucolaranja)
lab5 = tk.Label(tela1, image=foto5, bg="gray", bd=0)
lab5.place(rely=0.3, relx=0.75, anchor='s')

botaosucolaranja = Image.open("imagens\\bebidas\\botsucolaranja.png")
botaosucolaranja1 = ImageTk.PhotoImage(botaosucolaranja)
botaosucolaranja = tk.Label(tela1, image=botaosucolaranja1, bd=0)
botaosucolaranja.place(rely=0.32, relx=0.75, anchor='n')
botaosucolaranja.bind('<Button-1>', lambda e: print('Opa'))




### TELA 2           ======                      ==                     ==                   ==           ==



telat2 = tk.Frame(root, background='yellow')

# tPrincipal = tk.Frame(root, background='#ffff12')

telat2.grid(column=0, row=0, sticky='nsew')

titulotela = tk.Label(telat2, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulotela.place(rely=0.00, relx=0.5, anchor='n')

## PÃO AUSTRALIANO ==              ==                ==                 ==               == 


pao = Image.open("imagens\\bebidas\\entradas\\paoutback.png")
pao.thumbnail((300, 300))
fot1 = ImageTk.PhotoImage(pao)
label_pao = tk.Label(telat2, image=fot1, bg="gray", bd=0)
label_pao.place(rely=0.3, relx=0.75, anchor='s')

botaopao = Image.open("imagens\\bebidas\\entradas\\botpao.png")
botaopao1 = ImageTk.PhotoImage(botaopao)
botaopao = tk.Label(telat2, image=botaopao1, bd=0)
botaopao.place(rely=0.32, relx=0.75, anchor='n')
botaopao.bind('<Button-1>', lambda e: print('Opa'))

# # ALHEIRA

alheira = Image.open("imagens\\bebidas\\entradas\\alheira.png")
alheira.thumbnail((300, 300))
fotoalheira = ImageTk.PhotoImage(alheira)
label_alheira = tk.Label(telat2, image=fotoalheira, bg="gray", bd=0)
label_alheira.place(rely=0.3, relx=0.5, anchor='s')

botaoalheira = Image.open("imagens\\bebidas\\entradas\\botalheira.png")
botaoalheira1 = ImageTk.PhotoImage(botaoalheira)
botaoalheira = tk.Label(telat2, image=botaoalheira1, bd=0)
botaoalheira.place(rely=0.40, relx=0.5, anchor='s')
botaoalheira.bind('<Button-1>', lambda e: print('Opa'))


## quibebe ==             ==                      ==                         ==


quibebe = Image.open("imagens\\bebidas\\entradas\\quibebe.png")
quibebe.thumbnail((300, 300))
fotoquibebe = ImageTk.PhotoImage(quibebe)
label_quibebe = tk.Label(telat2, image=fotoquibebe, bg="gray", bd=0)
label_quibebe.place(rely=0.3, relx=0.25, anchor='s')

botaoquibebe = Image.open("imagens\\bebidas\\entradas\\botquibebe.png")
botaoquibebe1 = ImageTk.PhotoImage(botaoquibebe)
botaoquibebe = tk.Label(telat2, image=botaoquibebe1, bd=0)
botaoquibebe.place(rely=0.40, relx=0.25, anchor='s')
botaoquibebe.bind('<Button-1>', lambda e: print('Opa'))




antepasto = Image.open("imagens\\bebidas\\entradas\\antepasto.png")
antepasto.thumbnail((300, 300))
fotoantepasto = ImageTk.PhotoImage(antepasto)
labelantepasto = tk.Label(telat2, image=fotoantepasto, bg="gray", bd=0)
labelantepasto.place(rely=0.52, relx=0.35, anchor='n')

botaoantepasto = Image.open("imagens\\bebidas\\entradas\\botantepasto.png")
botaoantepasto1 = ImageTk.PhotoImage(botaoantepasto)
botaoantepasto = tk.Label(telat2, image=botaoantepasto1, bd=0)
botaoantepasto.place(rely=0.81, relx=0.35, anchor="s")
botaoantepasto.bind('<Button-1>', lambda e: print('Opa'))




bololegumes = Image.open("imagens\\bebidas\\entradas\\bololegumes.png")
bololegumes.thumbnail((300, 300))
bololegumes1 = ImageTk.PhotoImage(bololegumes)
labelbololegumes = tk.Label(telat2, image=bololegumes1, bg="gray", bd=0)
labelbololegumes.place(rely=0.52, relx=0.65, anchor='n')

botaobololegumes = Image.open("imagens\\bebidas\\entradas\\botbololegumes.png")
botaobololegumes1 = ImageTk.PhotoImage(botaobololegumes)
botaobololegumes = tk.Label(telat2, image=botaobololegumes1, bd=0)
botaobololegumes.place(rely=0.81, relx=0.65, anchor="s")
botaobololegumes.bind('<Button-1>', lambda e: print('Opa'))

## tela3 ==           ==                  ==                  ==                ==                     ==

telat3 = tk.Frame(root, background='#ffff12')
telat3.grid(column=0, row=0, sticky='nsew')

titulot3 = tk.Label(telat3, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulot3.place(rely=0.00, relx=0.5, anchor='n')

## gold label =          ==                  ==              ==              ==

goldlabel = Image.open("bebidalcolica\\goldlabel2.png")
goldlabel.thumbnail((300, 300))
goldlabel1 = ImageTk.PhotoImage(goldlabel)
labelgoldlabel = tk.Label(telat3, image=goldlabel1, bg="gray", bd=0)
labelgoldlabel.place(rely=0.4, relx=0.75, anchor='s')

botaogoldlabel = Image.open("bebidalcolica\\botaogoldlabel.png")
botaogoldlabel1 = ImageTk.PhotoImage(botaogoldlabel)
botaogoldlabel = tk.Label(telat3, image=botaogoldlabel1, bd=0)
botaogoldlabel.place(rely=0.42, relx=0.75, anchor="n")
botaogoldlabel.bind('<Button-1>', lambda e: print('Opa'))


## jack daniels ==             ==                        ==         ==


jackdaniels = Image.open("bebidalcolica\\jackdanielss.png")
jackdaniels.thumbnail((300, 300))
jackdaniels1 = ImageTk.PhotoImage(jackdaniels)
label_jackdaniels = tk.Label(telat3, image=jackdaniels1, bg="gray", bd=0)
label_jackdaniels.place(rely=0.4, relx=0.5, anchor='s')

botaojackdaniels = Image.open("bebidalcolica\\botaojackdenielss.png")
botaojackdaniels1 = ImageTk.PhotoImage(botaojackdaniels)
botaojackdaniels = tk.Label(telat3, image=botaojackdaniels1, bd=0)
botaojackdaniels.place(rely=0.50, relx=0.5, anchor='s')
botaojackdaniels.bind('<Button-1>', lambda e: print('Opa'))

## royal salute ==           ==                ==         == 



royalsalute = Image.open("bebidalcolica\\royalsalutee.png")
royalsalute.thumbnail((300, 300))
fotoroyalsalute = ImageTk.PhotoImage(royalsalute)
label_royalsalute = tk.Label(telat3, image=fotoroyalsalute, bg="gray", bd=0)
label_royalsalute.place(rely=0.4, relx=0.25, anchor='s')

# botaoroyalsalute = Image.open("bebidalcolica\\botaoroyasalute.png")
# botaoroyalsalute1 = ImageTk.PhotoImage(botaoroyalsalute)
# botaoquibebe = tk.Label(telat3, image=botaoroyalsalute1, bd=0)
# botaoroyalsalute.place(rely=0.20, relx=0.25, anchor='s')
# botaoroyalsalute.bind('<Button-1>', lambda e: print('Opa'))

## buchanans ==             ==                               ==              ==

buchanans = Image.open("bebidalcolica\\buchananss.png")
buchanans.thumbnail((300, 300))
fotobuchanans = ImageTk.PhotoImage(buchanans)
label_buchanans = tk.Label(telat3, image=fotobuchanans, bg="gray", bd=0)
label_buchanans.place(rely=0.57, relx=0.35, anchor='n')


botaobuchanans = Image.open("bebidalcolica\\botaobuchanans.png")
botaobuchanans1 = ImageTk.PhotoImage(botaobuchanans)
botaobuchanans = tk.Label(telat3, image=botaobuchanans1, bd=0)
botaobuchanans.place(rely=0.79, relx=0.35, anchor="n")
botaobuchanans.bind('<Button-1>', lambda e: print('Opa'))


## black label      =               =             =             =              = 

blacklabel = Image.open("bebidalcolica\\blacklabell.png")
blacklabel.thumbnail((300, 300))
fotoblacklabel = ImageTk.PhotoImage(blacklabel)
label_blacklabel = tk.Label(telat3, image=fotoblacklabel, bg="gray", bd=0)
label_blacklabel.place(rely=0.57, relx=0.65, anchor='n')

botaoblacklabel = Image.open("bebidalcolica\\botaoblacklabel.png")
botaoblacklabel1 = ImageTk.PhotoImage(botaoblacklabel)
botaoblacklabel = tk.Label(telat3, image=botaoblacklabel1, bd=0)
botaoblacklabel.place(rely=0.87, relx=0.65, anchor="n")
botaoblacklabel.bind('<Button-1>', lambda e: print('Opa'))

## TELA 4 ==            =               ==                ==               ==

telat4 = tk.Frame(root, background='#ffff12')
telat4.grid(column=0, row=0, sticky='nsew')

titulot4 = tk.Label(telat4, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulot4.place(rely=0.00, relx=0.5, anchor='n')

## lasanha ==             ==                   ==                 ==      


lasanha = Image.open("pratosprincipais\\lasanha.png")
lasanha.thumbnail((300, 300))
fotolasanha = ImageTk.PhotoImage(lasanha)
label_lasanha = tk.Label(telat4, image=fotolasanha, bg="gray", bd=0)
label_lasanha.place(rely=0.57, relx=0.65, anchor='n')

botaolasanha = Image.open("pratosprincipais\\botaolasanha (1).png")
botaolasanha1 = ImageTk.PhotoImage(botaolasanha)
botaolasanha = tk.Label(telat4, image=botaolasanha1, bd=0)
botaolasanha.place(rely=0.68, relx=0.65, anchor="n")
botaolasanha.bind('<Button-1>', lambda e: print('Opa'))


## feijoada ==             ==              ==          ==                  ==    

feijoada = Image.open("pratosprincipais\\feijoada.png")
feijoada.thumbnail((300, 300))
fotofeijoada = ImageTk.PhotoImage(feijoada)
label_feijoada = tk.Label(telat4, image=fotofeijoada, bg="gray", bd=0)
label_feijoada.place(rely=0.57, relx=0.35, anchor='n')

botaofeijoada = Image.open("pratosprincipais\\botaofeijoada (1).png")
botaofeijoada1 = ImageTk.PhotoImage(botaofeijoada)
botaofeijoada = tk.Label(telat4, image=botaofeijoada1, bd=0)
botaofeijoada.place(rely=0.69, relx=0.35, anchor="n")
botaofeijoada.bind('<Button-1>', lambda e: print('Opa'))



## camarao ==                ==                ==                ==         ==   


camarao = Image.open("pratosprincipais\\camarao.png")
camarao.thumbnail((300, 300))
fotocamarao = ImageTk.PhotoImage(camarao)
label_camarao = tk.Label(telat4, image=fotocamarao, bg="gray", bd=0)
label_camarao.place(rely=0.3, relx=0.25, anchor='s')

botaocamarao = Image.open("pratosprincipais\\botaocamarao (1).png")
botaocamarao1 = ImageTk.PhotoImage(botaocamarao)
botaocamarao = tk.Label(telat4, image=botaocamarao1, bd=0)
botaocamarao.place(rely=0.40, relx=0.25, anchor='s')
botaocamarao.bind('<Button-1>', lambda e: print('Opa'))



##  peixe frito ==                          = ====                           ==             ==  == 

peixefrito = Image.open("pratosprincipais\\peixefrito.png")
peixefrito.thumbnail((300, 300))
fotopeixefrito = ImageTk.PhotoImage(peixefrito)
label_peixefrito = tk.Label(telat4, image=fotopeixefrito, bg="gray", bd=0)
label_peixefrito.place(rely=0.3, relx=0.5, anchor='s')

botaopeixefrito = Image.open("pratosprincipais\\botaopeixefrito (1).png")
botaopeixefrito1 = ImageTk.PhotoImage(botaopeixefrito)
botaopeixefrito = tk.Label(telat4, image=botaopeixefrito1, bd=0)
botaopeixefrito.place(rely=0.40, relx=0.5, anchor='s')
botaopeixefrito.bind('<Button-1>', lambda e: print('Opa'))


## peixe assado           ==                      ==                          ==                     == 

peixeassado = Image.open("pratosprincipais\\peixeassado.png")
peixeassado.thumbnail((300, 300))
fotopeixeassado = ImageTk.PhotoImage(peixeassado)
label_peixeassado = tk.Label(telat4, image=fotopeixeassado, bg="gray", bd=0)
label_peixeassado.place(rely=0.3, relx=0.75, anchor='s')

botaopeixeassado = Image.open("pratosprincipais\\botaopeixeassado.png")
botaopeixeassado1 = ImageTk.PhotoImage(botaopeixeassado)
botaopeixeassado = tk.Label(telat4, image=botaopeixeassado1, bd=0)
botaopeixeassado.place(rely=0.40, relx=0.75, anchor='s')
botaopeixeassado.bind('<Button-1>', lambda e: print('Opa'))



## TELA 5  ==              ==                  == 


telat5 = tk.Frame(root, background='#ffff12')
telat5.grid(column=0, row=0, sticky='nsew')

titulot5 = tk.Label(telat5, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulot5.place(rely=0.00, relx=0.5, anchor='n')


## bolo de chocolate =              ==                    ==              ==              ==      


bolochocolate = Image.open("sobremesas\\bolochocolate.png")
bolochocolate.thumbnail((300, 300))
fotobolochocolate = ImageTk.PhotoImage(bolochocolate)
label_bolochocolate = tk.Label(telat5, image=fotobolochocolate, bg="gray", bd=0)
label_bolochocolate.place(rely=0.3, relx=0.75, anchor='s')

botaobolochocolate = Image.open("sobremesas\\botbolochocolate.png")
botaobolochocolate1 = ImageTk.PhotoImage(botaobolochocolate)
botaobolochocolate = tk.Label(telat5, image=botaobolochocolate1, bd=0)
botaobolochocolate.place(rely=0.37, relx=0.75, anchor='s')
botaobolochocolate.bind('<Button-1>', lambda e: print('Opa'))


## pudim ==             ==                     ==             == 


pudim = Image.open("sobremesas\\pudim.png")
pudim.thumbnail((300, 300))
fotopudim = ImageTk.PhotoImage(pudim)
label_pudim = tk.Label(telat5, image=fotopudim, bg="gray", bd=0)
label_pudim.place(rely=0.3, relx=0.5, anchor='s')

botaopudim = Image.open("sobremesas\\botaopudim.png")
botaopudim1 = ImageTk.PhotoImage(botaopudim)
botaopudim = tk.Label(telat5, image=botaopudim1, bd=0)
botaopudim.place(rely=0.37, relx=0.5, anchor='s')
botaopudim.bind('<Button-1>', lambda e: print('Opa'))


## torta de limão ==           ==             ==   

tortalimao = Image.open("sobremesas\\tortalimao.png")
tortalimao.thumbnail((300, 300))
fototortalimao = ImageTk.PhotoImage(tortalimao)
label_tortalimao = tk.Label(telat5, image=fototortalimao, bg="gray", bd=0)
label_tortalimao.place(rely=0.3, relx=0.25, anchor='s')

botaotortalimao = Image.open("sobremesas\\botaotortalimao.png")
botaotortalimao1 = ImageTk.PhotoImage(botaotortalimao)
botaotortalimao = tk.Label(telat5, image=botaotortalimao1, bd=0)
botaotortalimao.place(rely=0.37, relx=0.25, anchor='s')
botaotortalimao.bind('<Button-1>', lambda e: print('Opa'))


##  PAVE ==             ==               ==               ==  

pave = Image.open("sobremesas\\pave.png")
pave.thumbnail((300, 300))
fotopave = ImageTk.PhotoImage(pave)
label_pave = tk.Label(telat5, image=fotopave, bg="gray", bd=0)
label_pave.place(rely=0.57, relx=0.35, anchor='n')

botaopave = Image.open("sobremesas\\botaopave.png")
botaopave1 = ImageTk.PhotoImage(botaopave)
botaopave = tk.Label(telat5, image=botaopave1, bd=0)
botaopave.place(rely=0.71, relx=0.35, anchor="n")
botaopave.bind('<Button-1>', lambda e: print('Opa'))

## MOUSE DE MARACUJÁ ==             ==                  = =                      ==             ==


mousemaracuja = Image.open("sobremesas\\moussemaracuja.png")
mousemaracuja.thumbnail((300, 300))
fotomousemaracuja = ImageTk.PhotoImage(mousemaracuja)
label_mousemaracuja = tk.Label(telat5, image=fotomousemaracuja, bg="gray", bd=0)
label_mousemaracuja.place(rely=0.57, relx=0.65, anchor='n')

botaomousemaracuja = Image.open("sobremesas\\botaomoussemaracuja.png")
botaomousemaracuja1 = ImageTk.PhotoImage(botaomousemaracuja)
botaomousemaracuja = tk.Label(telat5, image=botaomousemaracuja1, bd=0)
botaomousemaracuja.place(rely=0.71, relx=0.65, anchor="n")
botaomousemaracuja.bind('<Button-1>', lambda e: print('Opa'))



## TELA 6  ==         = =                          ==                  == 


telat6 = tk.Frame(root, background='#ffff12')
telat6.grid(column=0, row=0, sticky='nsew')

titulot6 = tk.Label(telat6, text="Restaurante do Ederson", font=("Arial", 30, "bold"), anchor="center", background="yellow")
titulot6.place(rely=0.00, relx=0.5, anchor='n')


## salmao ==         ==              ==        

salmao = Image.open("menuchef\\salmao.png")
salmao.thumbnail((300, 300))
fotosalmao = ImageTk.PhotoImage(salmao)
label_salmao = tk.Label(telat6, image=fotosalmao, bg="gray", bd=0)
label_salmao.place(rely=0.57, relx=0.65, anchor='n')

botaosalmao = Image.open("menuchef\\botaosalmao.png")
botaosalmao1 = ImageTk.PhotoImage(botaosalmao)
botaosalmao = tk.Label(telat6, image=botaosalmao1, bd=0)
botaosalmao.place(rely=0.69, relx=0.65, anchor="n")
botaosalmao.bind('<Button-1>', lambda e: print('Opa'))


## FRANGO GRELHADO ==             ==                 == 

frangogrelhado = Image.open("menuchef\\frangogrelhado.png")
frangogrelhado.thumbnail((300, 300))
fotofrangogrelhado = ImageTk.PhotoImage(frangogrelhado)
label_frangogrelhado = tk.Label(telat6, image=fotofrangogrelhado, bg="gray", bd=0)
label_frangogrelhado.place(rely=0.57, relx=0.35, anchor='n')

frangogrelhado = Image.open("menuchef\\botaofrangogrelhado.png")
frangogrelhado1 = ImageTk.PhotoImage(frangogrelhado)
frangogrelhado = tk.Label(telat6, image=frangogrelhado1, bd=0)
frangogrelhado.place(rely=0.72, relx=0.35, anchor="n")
frangogrelhado.bind('<Button-1>', lambda e: print('Opa'))


# ## FRANGO ASSADO ==        ==           ==            ==           ==  

frangoassado = Image.open("menuchef\\frangoassado.png")
frangoassado.thumbnail((300, 300))
fotofrangoassado = ImageTk.PhotoImage(frangoassado)
label_frangoassado = tk.Label(telat6, image=fotofrangoassado, bg="gray", bd=0)
label_frangoassado.place(rely=0.3, relx=0.25, anchor='s')

frangoassado = Image.open("menuchef\\botaofrangoassado.png")
frangoassado1 = ImageTk.PhotoImage(frangoassado)
frangoassado = tk.Label(telat6, image=frangoassado1, bd=0)
frangoassado.place(rely=0.37, relx=0.25, anchor='s')
frangoassado.bind('<Button-1>', lambda e: print('Opa'))


# ## Costela Suína ==          == ====                               == 


costelasuina = Image.open("menuchef\\costelasuina.png")
costelasuina.thumbnail((300, 300))
fotocostelasuina = ImageTk.PhotoImage(costelasuina)
label_costelasuina = tk.Label(telat6, image=fotocostelasuina, bg="gray", bd=0)
label_costelasuina.place(rely=0.3, relx=0.5, anchor='s')

costelasuina = Image.open("menuchef\\botaocostelasuina.png")
costelasuina1 = ImageTk.PhotoImage(costelasuina)
costelasuina = tk.Label(telat6, image=costelasuina1, bd=0)
costelasuina.place(rely=0.37, relx=0.5, anchor='s')
costelasuina.bind('<Button-1>', lambda e: print('Opa'))



# ## BIFE A PARMEDIANA == = = == =             ==  

bifeparmediana = Image.open("menuchef\\bifeaparmegiana.png")
bifeparmediana.thumbnail((300, 300))
fotobifeparmediana = ImageTk.PhotoImage(bifeparmediana)
label_bifeparmediana = tk.Label(telat6, image=fotobifeparmediana, bg="gray", bd=0)
label_bifeparmediana.place(rely=0.3, relx=0.75, anchor='s')

bifeparmediana = Image.open("menuchef\\botaobifeparmediana.png")
bifeparmediana1 = ImageTk.PhotoImage(bifeparmediana)
bifeparmediana = tk.Label(telat6, image=bifeparmediana1, bd=0)
bifeparmediana.place(rely=0.37, relx=0.75, anchor='s')
bifeparmediana.bind('<Button-1>', lambda e: print('Opa'))


login()
root.mainloop()
 