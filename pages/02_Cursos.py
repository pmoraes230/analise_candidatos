import streamlit as st
from src.loader import carregar_dados
from src.config import COLUNA_CURSO, COLUNA_NOME, COLUNA_INSTRUTOR
from src.analysis import gerar_indicadores_curso
from src.charts import grafico_status_curso, grafico_instrutores_curso

st.title("Análise por Curso")

df = carregar_dados()

curso = st.selectbox(
    "Selecione um curso",
    sorted(df[COLUNA_CURSO].dropna().unique())
)

df_filtrado = df[df[COLUNA_CURSO] == curso]

if df_filtrado.empty:
    st.warning("Nenhum registro encontrado para o curso selecionado.")
else:
    indicadores = gerar_indicadores_curso(df_filtrado)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de candidatos", indicadores["total"])
    col2.metric("Elegíveis", indicadores["total_elegiveis"])
    col3.metric("Não elegíveis", indicadores["total_nao_elegiveis"])
    col4.metric(
        "Idade média",
        indicadores["idade_media"] if indicadores["idade_media"] is not None else "-"
    )

    st.markdown(f"**Instrutores diferentes neste curso:** {indicadores['total_instrutores']}")
    st.divider()

    col_graf1, col_graf2 = st.columns(2)
    with col_graf1:
        st.plotly_chart(grafico_status_curso(df_filtrado), use_container_width=True)
    with col_graf2:
        st.plotly_chart(grafico_instrutores_curso(df_filtrado), use_container_width=True)

    st.divider()
    st.subheader("Detalhes dos candidatos")
    st.dataframe(
        df_filtrado[[COLUNA_NOME, COLUNA_CURSO, COLUNA_INSTRUTOR, "Idade", "Situação"]],
        use_container_width=True
    )
