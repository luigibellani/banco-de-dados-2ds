import tkinter as tk
from tkinter import messagebox
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

# Configuração da interface gráfica
root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("350x220")

# Rótulos e campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_telefone = tk.Entry(root, width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

# Botões
btn_salvar = tk.Button(root, text="Salvar", command=salvar_cliente, width=12)
btn_salvar.grid(row=3, column=0, padx=10, pady=15)

btn_limpar = tk.Button(root, text="Limpar", command=limpar_formulario, width=12)
btn_limpar.grid(row=3, column=1, padx=10, pady=15, sticky="e")

root.mainloop()

# Fechar a conexão com o banco de dados ao encerrar o programa
conn.close()
