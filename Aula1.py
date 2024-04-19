from tkinter import *

janela = Tk()

class Aplicacao:
    def __init__(self):
        self.tela()
        self.frames_tela()
        janela.mainloop() # Mantem a janela aberta

    def tela(self):
        janela.title("Cadastro de clientes")
        janela.configure(background="#1f1f29")# Cor de fundo
        janela.geometry("800x600") # Tamanho da janela
        janela.resizable(width=True, height=True) # Não permite redimensionar a janela
        janela.maxsize(width=900, height=700) # Tamanho maximo da janela
        janela.minsize(width=500, height=300) # Tamanho minimo da janela

    def frames_tela(self):
        self.frame_1 = Frame(janela , bg = "#fffafa" , bd = 2 , highlightbackground = "#0492c2" , highlightthickness = 4)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)
        self.frame_2 = Frame(janela , bg = "#fffafa", bd = 2 , highlightbackground = "#0492c2" , highlightthickness = 4)
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)

Aplicacao()