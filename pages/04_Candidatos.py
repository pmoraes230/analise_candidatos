import streamlit as st
from src.loader import carregar_dados
from src.config import COLUNA_NOME, COLUNA_CURSO, COLUNA_INSTRUTOR

st.title("Consulta de Candidatos")

df = carregar_dados()

filtro_situacao = st.selectbox(
    "Filtrar por situação",
    ["Todos", "Elegível", "Não elegível"]
)

if filtro_situacao != "Todos":
    df = df[df["Situação"] == filtro_situacao]

busca = st.text_input("Pesquisar candidato")

if busca:
    df = df[
        df[COLUNA_NOME].str.contains(busca, case=False, na=False)
    ]

st.dataframe(
    df[[COLUNA_NOME, COLUNA_CURSO, COLUNA_INSTRUTOR, "Idade", "Situação"]],
    width="stretch"
)