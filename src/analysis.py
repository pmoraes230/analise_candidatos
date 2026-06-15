from src.config import COLUNA_CURSO, COLUNA_INSTRUTOR


def gerar_indicadores(df):
    elegiveis = df[df["Situação"] == "Elegível"]
    nao_elegiveis = df[df["Situação"] == "Não elegível"]

    return {
        "total_candidatos": len(df),
        "total_elegiveis": len(elegiveis),
        "total_nao_elegiveis": len(nao_elegiveis),
        "idade_media": round(df["Idade"].mean(), 1),
        "total_cursos": df[COLUNA_CURSO].nunique(),
        "total_instrutores": df[COLUNA_INSTRUTOR].nunique()
    }


def gerar_indicadores_curso(df):
    elegiveis = df[df["Situação"] == "Elegível"]
    nao_elegiveis = df[df["Situação"] == "Não elegível"]

    idade_media = None
    if df["Idade"].notna().any():
        idade_media = round(df["Idade"].mean(), 1)

    return {
        "total": len(df),
        "total_elegiveis": len(elegiveis),
        "total_nao_elegiveis": len(nao_elegiveis),
        "idade_media": idade_media,
        "total_instrutores": df[COLUNA_INSTRUTOR].nunique()
    }