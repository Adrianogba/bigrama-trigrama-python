"""Interface console para o preditor de palavras."""

from pathlib import Path

from bigrama import bigramas
from ngrama import carregar_corpus, garantir_recursos_nltk, prever_proxima
from trigrama import trigramas

CORPUS = Path(__file__).parent / "memorial_de_ayres.txt"


def main() -> None:
    garantir_recursos_nltk()
    tokens = carregar_corpus(CORPUS)

    print("Preditor de Palavras — Bigramas, Trigramas e N-gramas")
    print("Digite 2+ palavras para prever a próxima (ou 'sair' para encerrar).\n")

    while True:
        entrada = input(">>> ").strip()
        if entrada.lower() == "sair":
            break

        palavras = entrada.split()
        if len(palavras) < 2:
            print("Erro: digite pelo menos 2 palavras.\n")
            continue

        if len(palavras) == 2:
            sugestoes = bigramas(tokens, palavras)
        elif len(palavras) == 3:
            sugestoes = trigramas(tokens, palavras)
        else:
            sugestoes = prever_proxima(tokens, palavras)

        if sugestoes:
            print(f"Sugestões: {', '.join(sugestoes)}\n")
        else:
            print("Nenhuma sugestão encontrada na base de dados.\n")


if __name__ == "__main__":
    main()
