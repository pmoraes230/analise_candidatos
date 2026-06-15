import pandas as pd
import re
import unicodedata
from src.config import COLUNA_DATA_NASCIMENTO, MAPEAMENTO_COLUNAS, COLUNAS_FINAIS, COLUNA_NOME, COLUNA_INSTRUTOR, COLUNA_CURSO, MAPEAMENTO_INSTRUTORES, MAPEAMENTO_CURSOS
from src.rules import classificar_elegibilidade


def normalizar_coluna(coluna):
    """Remove acentos e converte para minúsculas"""
    coluna = coluna.strip().lower()
    coluna = unicodedata.normalize('NFKD', coluna)
    coluna = ''.join([c for c in coluna if not unicodedata.combining(c)])
    # Remove espaços extras
    coluna = ' '.join(coluna.split())
    return coluna


def normalizar_instrutor(instrutor):
    """Normaliza nome do instrutor removendo acentos e espaços extras"""
    if not isinstance(instrutor, str) or pd.isna(instrutor):
        return instrutor
    
    # Normaliza: remove acentos, converte para minúsculas, remove espaços extras
    normalizado = normalizar_coluna(instrutor)
    
    # Busca no mapeamento
    nome_correto = MAPEAMENTO_INSTRUTORES.get(normalizado, None)
    
    if nome_correto:
        return nome_correto
    else:
        # Se não encontrar no mapeamento, retorna título case
        return instrutor.strip().title()


def chave_normalizada(valor):
    """Cria uma chave estável para comparar textos vindos da planilha."""
    valor = normalizar_coluna(valor)
    valor = re.sub(r"[^a-z0-9]+", " ", valor)
    return " ".join(valor.split())


def normalizar_curso(curso):
    """Agrupa variações de escrita do mesmo curso."""
    if not isinstance(curso, str) or pd.isna(curso):
        return curso

    chave = chave_normalizada(curso)
    curso_correto = MAPEAMENTO_CURSOS.get(chave)

    if curso_correto:
        return curso_correto

    return " ".join(curso.strip().split()).title()


def calcular_idade(data_nascimento):
    if pd.isnull(data_nascimento):
        return None

    hoje = pd.Timestamp.today()

    return hoje.year - data_nascimento.year - (
        (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
    )


def tratar_dados(df):
    df = df.copy()

    # Normaliza nomes das colunas
    df.columns = df.columns.map(normalizar_coluna)
    
    # Aplica mapeamento de colunas
    df = df.rename(columns=MAPEAMENTO_COLUNAS)
    
    # Remove colunas duplicadas, mantendo a última ocorrência
    df = df.loc[:, ~df.columns.duplicated(keep='last')]

    # Remove nomes de alunos duplicados, mantendo a ultima ocorrência
    df = df.drop_duplicates(subset=COLUNA_NOME, keep='last')
    
    # Mantém apenas as colunas desejadas que existem
    colunas_existentes = [col for col in COLUNAS_FINAIS if col in df.columns]
    df = df[colunas_existentes]

    df[COLUNA_DATA_NASCIMENTO] = pd.to_datetime(
        df[COLUNA_DATA_NASCIMENTO],
        errors="coerce",
        dayfirst=True
    )

    df["Idade"] = df[COLUNA_DATA_NASCIMENTO].apply(calcular_idade)

    df["Situação"] = df["Idade"].apply(classificar_elegibilidade)
    
    # Limpeza de valores de texto - remove espaços extras
    for coluna in [COLUNA_NOME]:
        if coluna in df.columns:
            df[coluna] = df[coluna].str.strip() if df[coluna].dtype == 'object' else df[coluna]

    if COLUNA_CURSO in df.columns:
        df[COLUNA_CURSO] = df[COLUNA_CURSO].apply(normalizar_curso)
    
    # Normaliza nomes dos instrutores usando função de normalização
    if COLUNA_INSTRUTOR in df.columns:
        df[COLUNA_INSTRUTOR] = df[COLUNA_INSTRUTOR].apply(normalizar_instrutor)

    return df
