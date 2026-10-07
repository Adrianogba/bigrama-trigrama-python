"""Wrapper de conveniência para predição com bigramas (n=2)."""

from ngrama import prever_proxima


def bigramas(tokens: list[str], palavras: list[str], top_n: int = 3) -> list[str]:
    """Prevê a próxima palavra usando bigramas (contexto de 2 palavras).

    Raises:
        ValueError: Se *palavras* não contiver exatamente 2 elementos.
    """
    if len(palavras) != 2:
        raise ValueError(f"Bigramas exigem exatamente 2 palavras, recebeu {len(palavras)}.")
    return prever_proxima(tokens, palavras, top_n)
