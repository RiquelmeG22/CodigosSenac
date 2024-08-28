import tkinter as tk 
from PIL import Image, ImageTk




root = tk.Tk()
root.title('Galeria')
root.geometry("800x800")
root.title('Galeria')
root.resizable(width=False, height=False)
root.configure(background="gray")
image1 = Image.open("img1.jpg")
image1.thumbnail((300, 300))
photo = ImageTk.PhotoImage(image1)

img1 = tk.Frame(bg="gray", bd=0, highlightthickness=0)
img1.pack(pady=10)

label1 = tk.Label(img1, image=photo, bg="gray", bd=0)
label1.image = photo
label1.pack()


entry1 = tk.Entry(width=100)
entry1.pack(pady=5)
entry1.insert(0, "Escreva um comentário!!")


image2 = Image.open("img2.jpg")
image2.thumbnail((300, 300))
photo = ImageTk.PhotoImage(image2)


img2 = tk.Frame(bg='gray', bd=0, highlightthickness=0)
img2.pack(pady=10)


label2 = tk.Label(img2, image=photo, bg="gray", bd=0)
label2.image = photo
label2.pack()

entry2 = tk.Entry(width=100)
entry2.pack(pady=5)
entry2.insert(0, "Escreva um comentário!!")


img3 = Image.open("img3.jpg")
img3.thumbnail((300, 300))
photo = ImageTk.PhotoImage(img3)

img3 = tk.Frame(bg="gray", bd=0, highlightthickness=0)
img3.pack(pady=10)

label3 = tk.Label(img3, image=photo, bg="gray", bd=0)
label3.image = photo
label3.pack()

entry3 = tk.Entry(width=100)
entry3.pack(pady=5)
entry3.insert(0, "Escreva um comentário!!")



botao = tk.Button(root, text="Enviar", width=20,)
botao.pack(pady=20)







root.mainloop()