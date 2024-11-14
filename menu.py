import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from tkinter import messagebox

def submit_form(entry_nome, entry_idade, entry_altura):
    nome = entry_nome.get() # Captura o valor inserido no campo de entrada 'nome'
    idade = entry_idade.get()
    altura = entry_altura.get()
    print(f"{nome}, {idade}, {altura}")

    if not idade.isdigit() or not altura.isdigit():
        messagebox.showwarning('**Digite um Número válido', 'Por gentileza, digite um número válido')
        entry_idade.delete(0, tk.END)


def criar_formulario():
    app = ttk.Window("Formulário")
    app.geometry("500x500")
    style = Style(theme="darkly")


    # Frames
    nome = ttk.Frame(app)
    idade = ttk.Frame(app)
    altura = ttk.Frame(app)

    
    nome.pack(pady=18, padx=10, fill="x")
    idade.pack(pady=18, padx=10, fill="x")
    altura.pack(pady=18, padx=10, fill="x")

    # Label
    ttk.Label(nome, text="Nome:").pack(side=tk.LEFT, padx=5)
    ttk.Label(idade, text="Idade:").pack(side=tk.LEFT, padx=5)
    ttk.Label(altura, text="Altura:").pack(side=tk.LEFT, padx=5)

    # Entry
    entry_nome = ttk.Entry(nome)
    entry_nome.pack(side=tk.LEFT, fill="x", expand=True, padx=5)

    entry_idade = ttk.Entry(idade)
    entry_idade.pack(side=tk.LEFT, fill="x" ,expand=True, padx=5)

    entry_altura = ttk.Entry(altura)
    entry_altura.pack(side=tk.LEFT, fill="x" ,expand=True, padx=5)

    # Botão de envio
    submit_button = ttk.Button(app, text="Enviar", command=lambda: submit_form(entry_nome, entry_idade, entry_altura))
    submit_button.pack(pady=10)

    app.mainloop()

# Chama a função para criar o formulário
criar_formulario()