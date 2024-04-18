from tkinter import *

janela = Tk()

class Aplicacao:
    def __init__(self):
        self.tela()
        janela.mainloop() # Mantem a janela aberta

    def tela(self):
        janela.title("Cadastro de clientes")
        janela.configure(background="#1f1f29")# Cor de fundo
        janela.geometry("800x600") # Tamanho da janela
        janela.resizable(width=True, height=True) # Não permite redimensionar a janela
        janela.maxsize(width=900, height=700) # Tamanho maximo da janela
        janela.minsize(width=500, height=300) # Tamanho minimo da janela


Aplicacao()