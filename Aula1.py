from tkinter import *

janela = Tk()

class Aplicacao:
    def __init__(self):
        self.tela()
        self.frames_tela()
        self.criar_botoes()
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

    def criar_botoes(self):
        #botao apagar
        self.botao_apagar = Button(self.frame_1, text = "Limpar", bg = "#0492c2", fg = "#fffafa", bd = 3)
        self.botao_apagar.place(relx = 0.15, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        #botao buscar
        self.botao_buscar = Button(self.frame_1, text = "Buscar", bg = "#0492c2", fg = "#fffafa", bd = 3)
        self.botao_buscar.place(relx = 0.26, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        #botao novo
        self.botao_novo = Button(self.frame_1, text = "Novo", bg = "#0492c2", fg = "#fffafa", bd = 3)
        self.botao_novo.place(relx = 0.65, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        #botao alterar
        self.botao_alterar = Button(self.frame_1, text = "Alterar", bg = "#0492c2", fg = "#fffafa", bd = 3)
        self.botao_alterar.place(relx = 0.77, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        #botao excluir
        self.botao_excluir = Button(self.frame_1, text = "Excluir", bg = "#0492c2", fg = "#fffafa", bd = 3)
        self.botao_excluir.place(relx = 0.89, rely = 0.1, relwidth = 0.1, relheight = 0.15)

Aplicacao()