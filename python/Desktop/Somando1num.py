import tkinter as tk

count = 0
def riquelme():
    global count
    count += 1
    print(count)
    oi.configure(text=f'Clique no botão {count} ', foreground="red")
    kk.configure(text=f"Sair {count} ", background="blue")

root = tk.Tk()
root.title('Tela de Desktop')
root.geometry("880x800")

frm = tk.Frame(root, background='red')
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.columnconfigure(2, weight=1)
frm.rowconfigure(0, weight=1)
frm.rowconfigure(1, weight=1)
frm.rowconfigure(2, weight=1)
oi = tk.Label(frm, text="Clique no botão!", font=("Arial",30))
oi.grid(column=1, row=0)
kk = tk.Button(frm, text="Sair", width=20, command=riquelme)
kk.grid(column=1, row=1)

frm.pack(fill="both", padx=40, anchor='center', expand=True)
root.mainloop()