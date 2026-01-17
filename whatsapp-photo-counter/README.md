📑 Documento de Requisitos - Sistema Pateo Counter (2026)
1. Visão Geral
O Pateo Counter é uma aplicação web desenvolvida em Python para automatizar a contagem de veículos lavados a partir de registros de conversas do WhatsApp. O sistema elimina a necessidade de contagem manual, oferecendo relatórios precisos e gráficos de produtividade.

2. Requisitos de Ambiente (Software)
Para garantir o funcionamento do sistema em 2026, os seguintes componentes são necessários:
Linguagem: Python 3.10+
Framework de Interface: Streamlit
Processamento de Dados: Pandas
Bibliotecas Auxiliares: re (Regex) e datetime (Nativas do Python).

3. Requisitos Funcionais (O que o sistema faz)
RF01 - Upload de Log: O sistema deve permitir o upload de arquivos no formato .txt (padrão de exportação do WhatsApp).
RF02 - Filtro por Período: O usuário deve poder definir uma data inicial e uma data final para a busca.
RF03 - Identificação Inteligente: O sistema deve reconhecer automaticamente placas de veículos (padrão antigo e Mercosul) e arquivos de mídia (fotos/vídeos).
RF04 - Cálculo de Total: O sistema deve exibir a soma total de veículos lavados no período selecionado.
RF05 - Gráfico de Produtividade: O sistema deve gerar um gráfico de barras mostrando a quantidade de lavagens por dia.

4. Requisitos Não Funcionais (Qualidade e Performance)
RNF01 - Rapidez: O processamento de arquivos grandes deve ser concluído em poucos segundos.
RNF02 - Segurança de Dados: O sistema não deve armazenar o conteúdo das conversas permanentemente. Arquivos temporários devem ser deletados após o processamento.
RNF03 - Portabilidade: Por ser uma aplicação Web (Streamlit), o sistema deve funcionar em qualquer navegador (Chrome, Edge, Safari) no PC ou Celular.
RNF04 - Interface Intuitiva: O layout deve ser simples, focado em facilidade de uso para os funcionários da Pateo.

5. Regras de Negócio
RN01: Uma linha só é contabilizada se contiver uma data válida e o termo "Mídia" ou uma estrutura de placa veicular.
RN02: Se a data final informada for anterior à data inicial, o sistema deve exibir um aviso de erro ao usuário.

6. Instruções de Instalação (Para Desenvolvedores)
Certifique-se de ter o arquivo requirements.txt na pasta.
Execute a instalação das dependências:
pip install -r requirements.txt
Inicie a aplicação:
streamlit run app.py
