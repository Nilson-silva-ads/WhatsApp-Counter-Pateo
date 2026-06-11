# 🚗 WhatsApp Message & Photo Counter

Análise automatizada de logs de conversas do WhatsApp utilizando Expressões Regulares (Regex) e interface web interativa com Streamlit para otimização de fluxos operacionais e logísticos.

---

## 📝 Sobre o Projeto

Este projeto foi desenvolvido para solucionar um desafio real de conferência e auditoria logística (focado no fluxo de vistorias/logística da *Pateo Express Recife*). O objetivo principal é mitigar falhas humanas e eliminar o trabalho manual de contagem de veículos e registros operacionais reportados diariamente em grupos de conversas.

A aplicação processa o arquivo de exportação de dados do chat (`.txt`), realiza o *parsing* inteligente das mensagens através de padrões de **Regex** e apresenta métricas consolidadas instantaneamente por meio de um dashboard web ágil.

### 🔥 Principais Funcionalidades
- **Upload Dinâmico:** Processamento direto de arquivos `.txt` de logs de chats do WhatsApp.
- **Extração por Regex:** Identificação precisa de padrões textuais complexos que representam veículos e vistorias enviadas no fluxo.
- **Interface Intuitiva:** Exibição dos resultados consolidados em tempo real através de uma interface web minimalista.
- **Métricas Operacionais:** Relatório analítico automatizado que elimina o processo de contagem manual de mensagens.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Linguagem Principal:** Python 3.x
- **Interface do Usuário (UI):** [Streamlit](https://streamlit.io/)
- **Processamento de Texto:** Módulo Nativo `re` (Expressões Regulares / Regex)
- **Manipulação de Dados:** `pandas` (para organização e exibição dos dados coletados)

---

## 🧠 Desafios Técnicos Solucionados

O principal desafio técnico do projeto residiu na **padronização de dados não-estruturados**. Mensagens de chat do WhatsApp mudam de formato dependendo do sistema operacional do dispositivo que exportou o arquivo (Android vs. iOS) e da formatação livre utilizada pelos usuários.

A solução aplicada envolveu a construção de padrões robustos de Expressões Regulares para isolar o *timestamp* da mensagem, o autor e o conteúdo específico (como textos de mídia enviada ou descrições específicas de veículos), garantindo alta taxa de acerto na filtragem dos dados operacionais.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina (ou ambiente WSL2).

### 1. Clonar o Repositório
```bash
git clone [https://github.com/Nilson-silva-ads/WhatsApp-Counter-Pateo.git](https://github.com/Nilson-silva-ads/WhatsApp-Counter-Pateo.git)
cd WhatsApp-Counter-Pateo
