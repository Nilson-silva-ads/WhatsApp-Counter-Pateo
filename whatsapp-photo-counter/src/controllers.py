from .models import ContadorModel
from .views import PlacaView

class ContadorController:
    def __init__(self, caminho_arquivo):
        self.view = PlacaView(callback_contar=self.processar_solicitacao)

    def iniciar(self):
        self.view.mainloop()

    def processar_solicitacao(self, data_inicio, data_fim, caminho_arquivo):
        # Criamos o Model com o caminho que veio da interface
        model = ContadorModel(caminho_arquivo)
        dados = model.processar_dados(data_inicio, data_fim) #chamamos o processar dados com o intervalo.
        
        if dados is not None:
            total = len(dados)
            self.view.mostrar_resultado(f"✅ Total: {total} carros Lavados")
        else:
            self.view.mostrar_resultado("❌ Erro ao ler o arquivo.")