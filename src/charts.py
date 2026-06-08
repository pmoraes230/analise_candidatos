import plotly.express as px
from src.config import COLUNA_CURSO, COLUNA_INSTRUTOR


def grafico_cursos(df):
    dados = df[COLUNA_CURSO].value_counts().reset_index()
    dados.columns = ["Curso", "Quantidade"]

    return px.bar(
        dados,
        x="Quantidade",
        y="Curso",
        orientation="h",
        title="Quantidade de candidatos por curso"
    )


def grafico_instrutores(df):
    dados = df[COLUNA_INSTRUTOR].value_counts().reset_index()
    dados.columns = ["Instrutor", "Quantidade"]

    return px.pie(
        dados,
        names="Instrutor",
        values="Quantidade",
        title="Distribuição por instrutor"
    )


def grafico_idades(df):
    return px.histogram(
        df,
        x="Idade",
        nbins=10,
        title="Distribuição de idade dos candidatos"
    )