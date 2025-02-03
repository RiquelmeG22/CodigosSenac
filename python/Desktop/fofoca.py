import sqlite3

def create_database():
    conn = sqlite3.connect('fofocas.db')
    c = conn.cursor()

    # Tabelas
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            user_type TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS fofocas (
            id INTEGER PRIMARY KEY,
            title TEXT,
            text TEXT,
            image1 BLOB,
            image2 BLOB,
            image3 BLOB
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS points (
            user_id INTEGER,
            points INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            fofoca_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(fofoca_id) REFERENCES fofocas(id)
        )
    ''')

    conn.commit()
    conn.close()

create_database()
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

# Funções de Banco de Dados
def execute_query(query, params=()):
    conn = sqlite3.connect('fofocas.db')
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect('fofocas.db')
    c = conn.cursor()
    c.execute(query, params)
    result = c.fetchall()
    conn.close()
    return result

# Funções da Interface
def login():
    username = username_entry.get()
    password = password_entry.get()

    user = fetch_query('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    if user:
        user_type = user[0][3]
        if user_type == 'admin':
            show_admin_dashboard()
        elif user_type == 'famous':
            show_famous_dashboard()
        else:
            messagebox.showinfo("Info", "Login bem-sucedido como Cliente")
    else:
        messagebox.showerror("Erro", "Credenciais inválidas")

def show_admin_dashboard():
    admin_dashboard = tk.Toplevel()
    admin_dashboard.title("Dashboard Admin")
    tk.Label(admin_dashboard, text="Crie uma nova fofoca").pack()
    tk.Button(admin_dashboard, text="Sair", command=admin_dashboard.destroy).pack()

def show_famous_dashboard():
    famous_dashboard = tk.Toplevel()
    famous_dashboard.title("Dashboard Famoso")
    tk.Label(famous_dashboard, text="Reporte uma fofoca").pack()
    tk.Button(famous_dashboard, text="Sair", command=famous_dashboard.destroy).pack()

def register_user(user_type):
    username = username_entry.get()
    password = password_entry.get()
    execute_query('INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)', (username, password, user_type))
    messagebox.showinfo("Info", "Registro bem-sucedido")

def create_fofoca():
    title = title_entry.get()
    text = text_entry.get("1.0", tk.END)
    image1 = image1_entry.get()
    image2 = image2_entry.get()
    image3 = image3_entry.get()

    with open(image1, 'rb') as f:
        img1 = f.read()
    with open(image2, 'rb') as f:
        img2 = f.read()
    with open(image3, 'rb') as f:
        img3 = f.read()

    execute_query('INSERT INTO fofocas (title, text, image1, image2, image3) VALUES (?, ?, ?, ?, ?)', 
                  (title, text, img1, img2, img3))

    messagebox.showinfo("Info", "Fofoca criada com sucesso")

def main():
    root = tk.Tk()
    root.title("Sistema de Fofocas")

    global username_entry, password_entry, title_entry, text_entry, image1_entry, image2_entry, image3_entry

    tk.Label(root, text="Nome de Usuário").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Senha").pack()
    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    tk.Button(root, text="Login", command=login).pack()
    
    tk.Button(root, text="Registrar como Cliente", command=lambda: register_user('cliente')).pack()
    tk.Button(root, text="Registrar como Famoso", command=lambda: register_user('famous')).pack()
    tk.Button(root, text="Registrar como Admin", command=lambda: register_user('admin')).pack()

    tk.Label(root, text="Título da Fofoca").pack()
    title_entry = tk.Entry(root)
    title_entry.pack()

    tk.Label(root, text="Texto da Fofoca").pack()
    text_entry = tk.Text(root)
    text_entry.pack()

    tk.Label(root, text="Imagem 1").pack()
    image1_entry = tk.Entry(root)
    image1_entry.pack()

    tk.Label(root, text="Imagem 2").pack()
    image2_entry = tk.Entry(root)
    image2_entry.pack()

    tk.Label(root, text="Imagem 3").pack()
    image3_entry = tk.Entry(root)
    image3_entry.pack()

    tk.Button(root, text="Criar Fofoca", command=create_fofoca).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
