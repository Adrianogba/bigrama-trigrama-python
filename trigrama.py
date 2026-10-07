"""Wrapper de conveniência para predição com trigramas (n=3)."""

from ngrama import prever_proxima


def trigramas(tokens: list[str], palavras: list[str], top_n: int = 3) -> list[str]:
    """Prevê a próxima palavra usando trigramas (contexto de 3 palavras).

    Raises:
        ValueError: Se *palavras* não contiver exatamente 3 elementos.
    """
    if len(palavras) != 3:
        raise ValueError(f"Trigramas exigem exatamente 3 palavras, recebeu {len(palavras)}.")
    return prever_proxima(tokens, palavras, top_n)
