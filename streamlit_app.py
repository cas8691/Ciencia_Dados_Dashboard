# Importando as bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando os dados
dados = pd.read_excel('Vendas_Base_de_Dados.xlsx')
dados1 = pd.read_excel('Vendas_Base_de_Dados.xlsx')

# Exibindo informações e gráficos: mostrar o título do painel e exibir a tabela
st.title("Dashboard de Vendas")
st.write("Tabela de vendas do mês:")
st.dataframe(dados)

# Calcula o faturamento em cada linha
dados['Faturamento'] = dados['Quantidade'] * dados['Valor Unitário']
dados1['Faturamento'] = dados1['Quantidade'] * dados1['Valor Unitário']

# Agrupa e ordena o faturamento por loja (do maior para o menor)
dados = (
    dados.groupby('Loja')['Faturamento']
    .sum()
    .reset_index()
    .sort_values(by='Faturamento', ascending=False)
)

# Agrupa e ordena o faturamento por Produto (do maior para o menor)
dados1 = (
    dados1.groupby('Produto')['Faturamento']
    .sum()
    .reset_index()
    .sort_values(by='Faturamento', ascending=False)
)


# st.write(dados)

# Criar um gráfico barras de barras izza com o faturamento por loja
grafico = px.bar(dados, x='Loja', y='Faturamento', title='Faturamento por Loja')
st.plotly_chart(grafico)

#  Inserir um filtro para escolher uma loja e ver os dados dela
lojas = sorted(dados['Loja'].unique())
loja_escolhida = st.selectbox('Escolha a loja:', lojas)

dados_loja = dados[dados['Loja'] == loja_escolhida]
st.write(f'Dados da loja {loja_escolhida}:')
st.dataframe(dados_loja)


# Criar um gráfico de pizza com o faturamento por Produto
grafico = px.pie(
    dados1,
    names='Produto',
    values='Faturamento',
    title='Faturamento por Produto',
    hole=0,  # se quiser estilo donut, use um valor como 0.4
)
grafico.update_traces(textinfo='percent+label')
st.plotly_chart(grafico)

#===================================================================
#  Inserir um filtro para escolher um produto e ver os dados 
produtos = sorted(dados1['Produto'].unique())
produto_escolhido = st.selectbox('Escolha o Produto:', produtos)

dados_produto = dados1[dados1['Produto'] == produto_escolhido]
st.write(f'Dados do Produto {produto_escolhido}:')
st.dataframe(dados_produto)


# Agrupa e ordena o faturamento por produto (do maior para o menor)
dados1 = (
    dados1.groupby('Produto')['Faturamento']
    .sum()
    .reset_index()
    .sort_values(by='Faturamento', ascending=False)
)





