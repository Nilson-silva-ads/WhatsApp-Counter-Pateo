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
        self.input_data = ctk.CTkEntry(self, placeholder_text="Data (ex: 18/12/2025 ou 12/2025)", width=300)
        self.input_data.pack(pady=20)

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
        data = self.input_data.get()
        if not self.caminho_arquivo:
            self.mostrar_resultado("❌ Selecione um arquivo primeiro!")
            return
        if not data:
            self.mostrar_resultado("⚠️ Digite uma data!")
            return
        
        # Passa tanto a data quanto o arquivo para o Controller
        self.callback_contar(data, self.caminho_arquivo)

    def mostrar_resultado(self, mensagem):
        self.resultado_label.configure(text=mensagem)