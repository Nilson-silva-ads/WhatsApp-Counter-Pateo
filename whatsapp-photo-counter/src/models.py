import re
from datetime import datetime

#Cria a classe model com seus respequitivos padroes para buscar por palavras especificas usando o regex.
class ContadorModel:
    def __init__(self, arquivo_path):
        self.path = arquivo_path
        self.padrao_placa = r'[A-Z]{3}-?\d[A-Z]\d{2}'
        self.padrao_midia = r'Mídia'
        self.padrao_data = r'^(\d{2}/\d{2}/\d{4})' #regex para capturar a data no inicio da linha.

    def validar_data(self, data_texto):
        """Verifica se a string de data digitada pelo ususario é uma data valida."""
        try:
            datetime.strptime(data_texto, '%d/%m/%Y') #tenta converter para objeto datatime para validar calendario.
            return True
            #Se for apenas mes e ano.
        except ValueError:
            try:
                datetime.strptime(data_texto, '/%m/%Y')
            except ValueError:
                return False

    def processar_dados(self, filtro_data):
        """ Vasculha o arquivo e retorna apenas as linhas que batem com a data e o padrao.  """
        if not self.validar_data(filtro_data):
            print(f"Aviso: '{filtro_data}' não é um formato de data valido! DD/MM/AAAA ") #validação inicial para data do usuario.

        resultados = []
        try:
            with open(self.path, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    match_data = re.search(self.padrao_data, linha) #usando o regex para garantir que a data esta no lugar certo.
                    
                    if match_data and (filtro_data in match_data.group(1)): #Se encontrar uma data na linha e essa data contem o filtro solicitado.

                        #Verficação de placa ou midia (usando o ignorecase, para iginorar o jeito que o usuario escreve sendo maiusculo uo menusculo.)
                        achou_placa = re.search(self.padrao_placa, linha, re.IGNORECASE)
                        achou_midia = re.search(self.padrao_midia, linha, re.IGNORECASE) 

                        if achou_midia or achou_placa: #se achaou midia ou placa na linha.
                            resultados.append(linha.strip())
            return resultados
        except FileNotFoundError:
            return None