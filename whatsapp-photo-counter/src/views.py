import customtkinter as ctk
from tkinter import filedialog

class PlacaView(ctk.CTk):
    def __init__(self, callback_contar):
        super().__init__()
        self.title("WhatsApp Counter")
        self.geometry("500x400")
        self.callback_contar = callback_contar
        self.caminho_arquivo = None

        # Título
        ctk.CTkLabel(self, text="Sistema de Contagem Pateo", font=("Arial", 20, "bold")).pack(pady=20)

        # Seção de Seleção de Arquivo
        self.btn_arquivo = ctk.CTkButton(self, text="Selecionar Arquivo WhatsApp", command=self._selecionar_arquivo)
        self.btn_arquivo.pack(pady=10)
        
        self.label_arquivo = ctk.CTkLabel(self, text="Nenhum arquivo selecionado", font=("Arial", 10), text_color="gray")
        self.label_arquivo.pack(pady=5)

        # Entrada de Data
        self.frame_datas = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_datas.pack(pady=20)

        # Data Inicial
        self.label_ini = ctk.CTkLabel(self.frame_datas, text="Data Inicial:")
        self.label_ini.grid(row=0, column=0, padx=10)
        self.input_data_inicio = ctk.CTkEntry(self.frame_datas, placeholder_text="DD/MM/AAAA", width=120)
        self.input_data_inicio.grid(row=1, column=0, padx=10)

        # Data Final
        self.label_fim = ctk.CTkLabel(self.frame_datas, text="Data Final:")
        self.label_fim.grid(row=0, column=1, padx=10)
        self.input_data_fim = ctk.CTkEntry(self.frame_datas, placeholder_text="DD/MM/AAAA", width=120)
        self.input_data_fim.grid(row=1, column=1, padx=10)

        # Botão Processar
        self.btn_contar = ctk.CTkButton(self, text="Calcular Total", fg_color="green", hover_color="darkgreen", command=self._ao_clicar)
        self.btn_contar.pack(pady=10)

        # Resultado
        self.resultado_label = ctk.CTkLabel(self, text="", font=("Arial", 16, "bold"))
        self.resultado_label.pack(pady=20)

    def _selecionar_arquivo(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
        if caminho:
            self.caminho_arquivo = caminho
            nome_arquivo = caminho.split("/")[-1] # Pega só o nome para não ocupar a tela toda
            self.label_arquivo.configure(text=f"Arquivo: {nome_arquivo}", text_color="white")

    def _ao_clicar(self):
        # Pegamos os valores dos dois novos campos
        data_ini = self.input_data_inicio.get()
        data_fim = self.input_data_fim.get()

        if not self.caminho_arquivo:
            self.mostrar_resultado("❌ Selecione um arquivo primeiro!")
            return
        
        if not data_ini or not data_fim:
            self.mostrar_resultado("⚠️ Preencha as duas datas!")
            return
        
        # Passa tanto a data quanto o arquivo para o Controller
        self.callback_contar(data_ini, data_fim, self.caminho_arquivo)

    def mostrar_resultado(self, mensagem):
        self.resultado_label.configure(text=mensagem)