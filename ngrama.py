"""Motor genérico de n-gramas para predição de palavras."""

from collections import Counter
from pathlib import Path

import nltk
from nltk.tokenize import word_tokenize


def garantir_recursos_nltk() -> None:
    """Baixa recursos do NLTK necessários, caso ainda não existam."""
    for recurso in ("punkt", "punkt_tab", "stopwords", "rslp"):
        nltk.download(recurso, quiet=True)


def carregar_corpus(caminho: Path | str) -> list[str]:
    """Lê um arquivo de texto e retorna a lista de tokens."""
    texto = Path(caminho).read_text(encoding="utf-8").replace("\n", " ")
    texto_limpo = texto.replace(",", " ").replace(".", " ")
    return word_tokenize(texto_limpo)


def prever_proxima(
    tokens: list[str],
    palavras: list[str],
    top_n: int = 3,
) -> list[str]:
    """Prevê as próximas palavras mais prováveis dado um contexto de *n* palavras.

    Funciona como n-grama genérico:
      - 2 palavras → bigrama
      - 3 palavras → trigrama
      - n palavras → n-grama

    Retorna até *top_n* sugestões ordenadas por frequência.
    """
    n = len(palavras)
    contexto = [p.lower() for p in palavras]
    proximas: list[str] = []

    for i in range(len(tokens) - n):
        janela = [tokens[i + j].lower() for j in range(n)]
        if janela == contexto:
            proximas.append(tokens[i + n])

    return [palavra for palavra, _ in Counter(proximas).most_common(top_n)]
