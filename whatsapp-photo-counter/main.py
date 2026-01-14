from src.controllers import ContadorController
from pathlib import Path

CAMINHO = Path("C:/Users/neojb/Desktop/Programaçao/Projetos/Projeto_contador_carros/whatsapp-photo-counter/data/Conversa do WhatsApp com Pateo Express RECIFE..txt")

def main():
    # 1. Instancia o controlador (que por sua vez criará a View)
    app = ContadorController(CAMINHO)
    
    # 2. Inicia o loop da interface gráfica
    app.iniciar()

if __name__ == "__main__":
    main()