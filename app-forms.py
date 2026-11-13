import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')
conn.commit()

# Função para limpar o formulário
def limpar_formulario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# Função para salvar os dados do cliente no banco de dados
def salvar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        cursor.execute('INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))
        conn.commit()
        messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        limpar_formulario()
    else:
        messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

# Função para visualizar os dados dos clientes
def visualizar_clientes():
    janela_visualizacao = tk.Toplevel()
    janela_visualizacao.title("Clientes Cadastrados")
    janela_visualizacao.geometry("500x300")

    tree = ttk.Treeview(janela_visualizacao, columns=("ID", "Nome", "Email", "Telefone"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Email", text="Email")
    tree.heading("Telefone", text="Telefone")
    
    tree.column("ID", width=40)
    tree.column("Nome", width=150)
    tree.column("Email", width=180)
    tree.column("Telefone", width=110)
    
    tree.pack(fill=tk.BOTH, expand=True)

    cursor.execute('SELECT * FROM clientes')
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("380x230")

# Rótulos e campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome = tk.Entry(root, width=32)
entry_nome.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(root, width=32)
entry_email.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_telefone = tk.Entry(root, width=32)
entry_telefone.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# Botões
btn_salvar = tk.Button(root, text="Salvar", command=salvar_cliente, width=10)
btn_salvar.grid(row=3, column=0, padx=10, pady=15)

btn_limpar = tk.Button(root, text="Limpar", command=limpar_formulario, width=10)
btn_limpar.grid(row=3, column=1, padx=5, pady=15)

btn_visualizar = tk.Button(root, text="Visualizar Clientes", command=visualizar_clientes, width=15)
btn_visualizar.grid(row=3, column=2, padx=10, pady=15)

root.mainloop()

# Fechar a conexão com o banco de dados ao encerrar o programa
conn.close()
