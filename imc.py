from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph

def pdf():
    pdf = canvas.Canvas(f'./FichaCadastral{nome.strip()}.pdf', pagesize=A4)
    pdf.drawCentredString(300, 800, f'Ficha Cadastral - {nome}')
    pdf.drawString(50, 700, f'Nome: {nome}')
    pdf.drawString(50, 680, f'Idade: {idade}')
    pdf.drawString(50, 660, f'Peso: {peso}')
    pdf.drawString(50, 640, f'Altura: {altura}')
    pdf.drawString(250, 580, f'Seu IMC é: {imc}')
    paragrafo = Paragraph('O índice de massa corporal (IMC) de um adulto é o seu peso em quilos, dividido por sua altura ao quadrado.')
    paragrafo.wrapOn(pdf, 400, 100)
    paragrafo.drawOn(pdf, 100, 400)
    pdf.drawInlineImage("https://static.wixstatic.com/media/36d7bf_0dfcfa43bacc4057bb9a3aaa7ea5204e~mv2.png/v1/fill/w_740,h_416,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/36d7bf_0dfcfa43bacc4057bb9a3aaa7ea5204e~mv2.png", 17, -25, width=565, height=305)
    pdf.save()  


print('Antes de comerçamos, precisamos de alguns dados:')
nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura ** 2)
print(imc)
imc = round(imc,2)

pdf()



