import os
import pandas as pd
import streamlit as st
from src.cleaner import tratar_dados

CAMINHO_BASE = "data/candidatos.xlsx"


@st.cache_data
def carregar_dados_cache(caminho, data_modificacao):
    df = pd.read_excel(caminho)
    return tratar_dados(df)


def carregar_dados():
    data_modificacao = os.path.getmtime(CAMINHO_BASE)
    return carregar_dados_cache(CAMINHO_BASE, data_modificacao)