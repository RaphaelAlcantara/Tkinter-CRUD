from tkinter import *

janela = Tk()

class Aplicacao:
    def __init__(self):
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        janela.mainloop() # Mantem a janela aberta

    def tela(self):
        janela.title("Cadastro de clientes")
        janela.configure(background="#1f1f29")# Cor de fundo
        janela.geometry("800x600") # Tamanho da janela
        janela.resizable(width=True, height=True) # Não permite redimensionar a janela
        janela.maxsize(width=900, height=800) # Tamanho maximo da janela
        janela.minsize(width=600, height=700) # Tamanho minimo da janela

    def frames_tela(self):
        self.frame_1 = Frame(janela , bg = "#fffafa" , bd = 2 , highlightbackground = "#0492c2" , highlightthickness = 4)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)
        self.frame_2 = Frame(janela , bg = "#fffafa", bd = 2 , highlightbackground = "#0492c2" , highlightthickness = 4)
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)

    def widgets_frame1(self):
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

        #Label e entrada código
        self.label_codigo = Label(self.frame_1, text = "Código", bg = "#fffafa")
        self.label_codigo.place(relx = 0.05, rely = 0.05)

        self.input_codigo = Entry(self.frame_1, bg = "#fffafa", bd = 2, fg = "#000000")
        self.input_codigo.place(relx = 0.05, rely = 0.15, relwidth = 0.08)

        #Label e entrada nome
        self.label_nome = Label(self.frame_1, text = "Nome", bg = "#fffafa")
        self.label_nome.place(relx = 0.05, rely = 0.45)

        self.input_nome = Entry(self.frame_1, bg = "#fffafa", bd = 2, fg = "#000000")
        self.input_nome.place(relx = 0.05, rely = 0.55, relwidth = 0.8)

        #Label e entrada telefone
        self.label_telefone = Label(self.frame_1, text = "Telefone", bg = "#fffafa")
        self.label_telefone.place(relx = 0.05, rely = 0.65)

        self.input_telefone = Entry(self.frame_1, bg = "#fffafa", bd = 2, fg = "#000000")
        self.input_telefone.place(relx = 0.05, rely = 0.75, relwidth = 0.3)

        #Label Cidade
        self.label_cidade = Label(self.frame_1, text = "Cidade", bg = "#fffafa")
        self.label_cidade.place(relx = 0.4, rely = 0.65)

        #input Cidade
        self.input_cidade = Entry(self.frame_1, bg = "#fffafa", bd = 2, fg = "#000000")
        self.input_cidade.place(relx = 0.4, rely = 0.75, relwidth = 0.45)




Aplicacao()