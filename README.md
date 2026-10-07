# Preditor de Palavras — Bigramas, Trigramas e N-gramas

Programa simples de predição da próxima palavra usando n-gramas sobre um corpus em texto (`.txt`).

## Estrutura

| Arquivo | Descrição |
|---|---|
| `ngrama.py` | Motor genérico de n-gramas (funciona para qualquer *n*) |
| `bigrama.py` | Wrapper para bigramas (contexto de 2 palavras) |
| `trigrama.py` | Wrapper para trigramas (contexto de 3 palavras) |
| `console.py` | Interface interativa via terminal |
| `tkinter_gui.pyw` | Interface gráfica com tkinter |
| `memorial_de_ayres.txt` | Corpus de exemplo (Machado de Assis) |

## Requisitos

- Python 3.12+
- NLTK

```bash
pip install -r requirements.txt
```

## Como usar

### Console

```bash
python console.py
```

Digite 2 ou mais palavras e o programa sugere a próxima:

```
>>> a casa
Sugestões: de, do, da
```

### Interface gráfica

```bash
python tkinter_gui.pyw
```

## Como funciona

O programa tokeniza o corpus e, dado um contexto de *n* palavras, procura todas as ocorrências dessa sequência no texto. A palavra seguinte mais frequente é retornada como sugestão.

- **Bigrama**: contexto de 2 palavras → `bigrama.py`
- **Trigrama**: contexto de 3 palavras → `trigrama.py`
- **N-grama**: contexto de *n* palavras → `ngrama.py`
