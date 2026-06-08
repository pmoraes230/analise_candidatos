import streamlit as st
from src.loader import carregar_dados
from src.config import COLUNA_CURSO

st.title("Análise por Curso")

df = carregar_dados()

curso = st.selectbox(
    "Selecione um curso",
    sorted(df[COLUNA_CURSO].dropna().unique())
)

df_filtrado = df[df[COLUNA_CURSO] == curso]

st.metric("Total neste curso", len(df_filtrado))
st.dataframe(df_filtrado)