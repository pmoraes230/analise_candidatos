import streamlit as st
from src.loader import carregar_dados
from src.config import COLUNA_INSTRUTOR

st.title("Análise por Instrutor")

df = carregar_dados()

instrutor = st.selectbox(
    "Selecione um instrutor",
    sorted(df[COLUNA_INSTRUTOR].dropna().unique())
)

df_filtrado = df[df[COLUNA_INSTRUTOR] == instrutor]

st.metric("Total de alunos vinculados", len(df_filtrado))
st.dataframe(df_filtrado)