import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mercado Imobiliário de Petrópolis", layout="wide")

st.title("📊 Análise Exploratória Imobiliária — Petrópolis (2024–2026)")
st.subheader("Apoio a Microempreendedores Habitacionais e Moradores de Áreas Periféricas (ACMIP / UCP)")

@st.cache_data
def carregar_dados():
    return pd.read_csv('data/processed/imoveis_petropolis_clean.csv')

df = carregar_dados()

regiao_selecionada = st.sidebar.selectbox("Selecione a Região / Distrito:", df['distrito'].unique())

df_filtrado = df[df['distrito'] == regiao_selecionada]

col1, col2, col3 = st.columns(3)
col1.metric("Preço Médio por m²", f"R$ {df_filtrado['preco_m2'].mean():,.2f}")
col2.metric("Mediana por m²", f"R$ {df_filtrado['preco_m2'].median():,.2f}")
col3.metric("Total de Anúncios na Região", len(df_filtrado))

st.write("### Tabela de Anúncios Filtrados por Bairro")
st.dataframe(df_filtrado[['bairro', 'area_m2', 'preco_venda', 'preco_m2', 'quartos']])
