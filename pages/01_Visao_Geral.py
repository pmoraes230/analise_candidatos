import streamlit as st
from src.loader import carregar_dados
from src.analysis import gerar_indicadores
from src.charts import grafico_cursos, grafico_instrutores

st.title("Visão Geral")

df = carregar_dados()
indicadores = gerar_indicadores(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de candidatos", indicadores["total_candidatos"])
col2.metric("Elegíveis", indicadores["total_elegiveis"])
col3.metric("Não elegíveis", indicadores["total_nao_elegiveis"])
col4.metric("Idade média", indicadores["idade_media"])

st.divider()

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.plotly_chart(grafico_cursos(df), use_container_width='stretch')

with col_graf2:
    st.plotly_chart(grafico_instrutores(df), use_container_width='stretch')