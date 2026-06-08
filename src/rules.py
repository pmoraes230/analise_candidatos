IDADE_MAXIMA_COMPETIDOR = 21


def classificar_elegibilidade(idade):
    if idade is None:
        return "Data inválida"

    if idade <= IDADE_MAXIMA_COMPETIDOR:
        return "Elegível"

    return "Não elegível"