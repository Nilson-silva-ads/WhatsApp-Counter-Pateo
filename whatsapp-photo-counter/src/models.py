import re
from datetime import datetime

#Cria a classe model com seus respequitivos padroes para buscar por palavras especificas usando o regex.
class ContadorModel:
    def __init__(self, arquivo_path):
        self.path = arquivo_path
        self.padrao_placa = r'[A-Z]{3}-?\d[A-Z]\d{2}'
        self.padrao_midia = r'Mídia'
        self.padrao_data = r'^(\d{2}/\d{2}/\d{4})' #regex para capturar a data no inicio da linha.

    def converter_para_data(self, data_texto):
        """Tenta converter uma string DD/MM/AAAA em objeto datetime."""
        try:
            return datetime.strptime(data_texto, '%d/%m/%Y')
        except ValueError:
            return None

    def processar_dados(self, data_inicio, data_fim):
        """ Vasculha o arquivo e retorna linhas dentro do intervalo de datas. """
        # 1. Converte as datas de busca para objetos comparáveis
        dt_inicio = self.converter_para_data(data_inicio)
        dt_fim = self.converter_para_data(data_fim)

        if not dt_inicio or not dt_fim:
            print('Erro: Uma das datas fornecidas é invalida. Use DD/MM/AAAA')
            return []
       
        resultados = []
        try:
            with open(self.path, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    match_data = re.search(self.padrao_data, linha) #usando o regex para garantir que a data esta no lugar certo.
                    
                    if match_data:
                        data_da_linha = self.converter_para_data(match_data.group(1)) #Converte data que esta na linha do whatsApp.
                        
                        if data_da_linha and (dt_inicio <= data_da_linha <= dt_fim): #comparando se o valor inicial e menor que o valor final.

                            #Verficação de placa ou midia (usando o ignorecase, para iginorar o jeito que o usuario escreve sendo maiusculo uo menusculo.)
                            achou_placa = re.search(self.padrao_placa, linha, re.IGNORECASE)
                            achou_midia = re.search(self.padrao_midia, linha, re.IGNORECASE) 

                            if achou_midia or achou_placa: #se achaou midia ou placa na linha.
                             resultados.append(linha.strip())
            return resultados
        except FileNotFoundError:
            return None