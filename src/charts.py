import plotly.express as px
from src.config import COLUNA_CURSO, COLUNA_INSTRUTOR


def grafico_cursos(df):
    dados = df[COLUNA_CURSO].value_counts().sort_values(ascending=True).reset_index()
    dados.columns = ["Curso", "Quantidade"]

    altura = max(420, min(720, 120 + (len(dados) * 42)))

    fig = px.bar(
        dados,
        x="Quantidade",
        y="Curso",
        orientation="h",
        text="Quantidade",
        title="Candidatos por curso",
        color="Quantidade",
        color_continuous_scale="Teal"
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False,
        hovertemplate="<b>%{y}</b><br>Candidatos: %{x}<extra></extra>"
    )
    fig.update_layout(
        height=altura,
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=20, r=40, t=60, b=30),
        xaxis_title="Candidatos",
        yaxis_title=None,
        bargap=0.24,
        title_x=0.02,
    )
    fig.update_xaxes(dtick=1, rangemode="tozero")

    return fig


def grafico_instrutores(df):
    dados = df[COLUNA_INSTRUTOR].value_counts().reset_index()
    dados.columns = ["Instrutor", "Quantidade"]

    return px.pie(
        dados,
        names="Instrutor",
        values="Quantidade",
        title="Distribuição por instrutor"
    )


def grafico_status_curso(df):
    dados = df["Situação"].value_counts().reset_index()
    dados.columns = ["Situação", "Quantidade"]

    return px.pie(
        dados,
        names="Situação",
        values="Quantidade",
        title="Situação dos candidatos"
    )


def grafico_instrutores_curso(df):
    dados = df[COLUNA_INSTRUTOR].value_counts().reset_index()
    dados.columns = ["Instrutor", "Quantidade"]

    return px.bar(
        dados,
        x="Quantidade",
        y="Instrutor",
        orientation="h",
        title="Instrutores no curso"
    )


def grafico_idades(df):
    return px.histogram(
        df,
        x="Idade",
        nbins=10,
        title="Distribuição de idade dos candidatos"
    )
