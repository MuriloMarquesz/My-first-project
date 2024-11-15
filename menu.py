import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph

def criar_formulario():
    app = ttk.Window("Formulário", size=(500, 500))
    style = Style(theme="darkly")

    def criar_pdf(nome, idade, peso, altura):
        pdf = canvas.Canvas(f'./FichaCadastral{nome}.pdf', pagesize=A4)
        pdf.drawCentredString(300, 800, f'Ficha Cadastral - {nome}')
        pdf.drawString(50, 700, f'Nome: {nome}')
        pdf.drawString(50, 680, f'Idade: {idade}')
        pdf.drawString(50, 660, f'Peso: {peso}')
        pdf.drawString(50, 640, f'Altura: {altura}')
        imc = peso / (altura ** 2)
        imc = round(imc, 2)
        pdf.drawString(250, 580, f'Seu IMC é: {imc}')
        paragrafo = Paragraph('O índice de massa corporal (IMC) de um adulto é o seu peso em quilos, dividido por sua altura ao quadrado.')
        paragrafo.wrapOn(pdf, 400, 100)
        paragrafo.drawOn(pdf, 100, 400)
        pdf.drawInlineImage("https://static.wixstatic.com/media/36d7bf_0dfcfa43bacc4057bb9a3aaa7ea5204e~mv2.png/v1/fill/w_740,h_416,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/36d7bf_0dfcfa43bacc4057bb9a3aaa7ea5204e~mv2.png", 17, -25, width=565, height=305)
        pdf.save()  

    def criar_entrada(label_text):
        frame = ttk.Frame(app)
        label = ttk.Label(frame, text=label_text)
        entry = ttk.Entry(frame)
        label.pack(side=tk.LEFT, padx=5)
        entry.pack(side=tk.LEFT, fill="x", expand=True, padx=5)
        frame.pack(pady=10, padx=10, fill="x")
        return entry

    # Campos de entrada
    entry_nome = criar_entrada("Nome:")
    entry_idade = criar_entrada("Idade:")
    entry_altura = criar_entrada("Altura:")
    entry_peso = criar_entrada("Peso:")

    # Label para exibir o IMC
    label_imc = ttk.Label(app, text="", font=("Helvetica", 14))
    label_imc.pack(pady=10)

    def submit_form():
        nome = entry_nome.get()
        idade = entry_idade.get()
        altura = entry_altura.get()
        peso = entry_peso.get()
        # Validação dos campos
        if not nome or not idade or not altura or not peso:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
            return
        if not idade.isdigit():
            messagebox.showwarning("Erro", "A idade deve ser um número válido.")
            return
        try:
            altura = float(altura)
            peso = float(peso)
        except ValueError:
            messagebox.showwarning("Erro", "A altura e o peso devem ser números válidos.")
            return
        if altura <= 0 or peso <= 0:
            messagebox.showwarning("Erro", "A altura e o peso devem ser valores positivos.")
            return

        criar_pdf(nome, idade, peso, altura)
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        imc = round(imc, 2)

        # IMC no label
        label_imc.config(text=f"Seu IMC é: {imc}")

    submit_button = ttk.Button(app, text="Enviar", command=submit_form)
    submit_button.pack(pady=20)

    app.mainloop()


# Chama a função para criar o formulário
criar_formulario()
