import streamlit as st
from src.models import ContadorModel
import os
import pandas as pd 

st.set_page_config(page_title="Pateo Counter", page_icon="🚗")

st.title("🚗 Sistema Contagem Pateo Express")
st.markdown("Faça o upload do arquivo WhatsApp para contar os carros lavados.")

arquivo_postado = st.file_uploader("Selecione o arquivo.txt do WhatsApp", type=['txt']) #Upload do arquivo.

#Entradas de Data lado a lado.
col1, col2 = st.columns(2)
with col1:
    data_ini = st.text_input("Data inicial", placeholder="DD/MM/AAAA")
with col2:
    data_fim = st.text_input("Data final", placeholder="DD/MM/AAAA")

#botao de processar.
if st.button("Buscar", type="primary"):
    if arquivo_postado is not None and data_ini and data_fim:
        #Salvando de forma temporaria para o model processar.
        caminho_temp = "temp_whatsapp.txt"
        with open(caminho_temp, 'wb') as f:
            f.write(arquivo_postado.getbuffer())


        with open(caminho_temp, 'r', encoding='utf-8') as f:
           
            #Instanciando a model.
            model = ContadorModel(caminho_temp)
            dados = model.processar_dados(data_ini, data_fim)

            if dados is not None:
                total = len(dados)
                st.success(f"### ✅ Total: {total} carros Lavados ")

                if len(dados) == 0:
                    st.error("Data não existe no arquivo ou não houve lavagem nesta data.")

                #Criando um grafico para os dados.
                #transformando lista de dados em um DataFrame(tablea)
                df = pd.DataFrame(dados, columns=['Data'])

                #converter para um formato de data real caso não estaje.
                #df['Data'] = pd.to_datetime(df['Data']).dt.date

                #contamos quantas vezes cada data aparece.
                contagem_por_dia = df['Data'].value_counts().sort_index()

                #exibindo o grafico de barras.
                st.subheader("📊 Lavagens por Dia")
                st.bar_chart(contagem_por_dia)
                
            else:
                st.error("Erro ao processar os dados. Verificar o formato das datas.")

        #limpando o arquivo temporario.
        if os.path.exists(caminho_temp):
            os.remove(caminho_temp)
    else:
        st.warning("⚠️ Por favor, selecione o arquivo e preencha as duas datas.")