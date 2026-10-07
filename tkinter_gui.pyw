"""Interface gráfica (tkinter) para o preditor de palavras."""

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from bigrama import bigramas
from ngrama import carregar_corpus, garantir_recursos_nltk, prever_proxima
from trigrama import trigramas

CORPUS = Path(__file__).parent / "memorial_de_ayres.txt"


def sobre() -> None:
    """Exibe informações sobre o programa."""
    messagebox.showinfo(
        "Sobre o Preditor de Palavras",
        "Preditor de palavras usando bigramas, trigramas e n-gramas "
        "para sugerir a próxima palavra a partir de uma sequência informada.",
    )


def criar_callback_adivinhar(tokens: list[str], var_texto: tk.StringVar):
    """Cria o callback de predição vinculado aos tokens carregados."""

    def adivinhar(*_args) -> None:
        palavras = var_texto.get().split()

        if len(palavras) < 2:
            messagebox.showerror("Erro", "Digite pelo menos 2 palavras.")
            return

        if len(palavras) == 2:
            sugestoes = bigramas(tokens, palavras)
        elif len(palavras) == 3:
            sugestoes = trigramas(tokens, palavras)
        else:
            sugestoes = prever_proxima(tokens, palavras)

        if sugestoes:
            messagebox.showinfo(
                "Sugestões",
                f"Sugestões para '{var_texto.get()}':\n\n{', '.join(sugestoes)}",
            )
        else:
            messagebox.showwarning(
                "Sem resultados",
                "Nenhuma sugestão encontrada na base de dados.",
            )

    return adivinhar


def main() -> None:
    garantir_recursos_nltk()
    tokens = carregar_corpus(CORPUS)

    root = tk.Tk()
    root.title("Preditor de Palavras — By Adriano Martins")

    # --- Menu ---
    menu = tk.Menu(root)
    root.config(menu=menu)

    menu_arquivo = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Arquivo", menu=menu_arquivo)
    menu_arquivo.add_command(label="Sair", command=root.quit)

    menu_ajuda = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Ajuda", menu=menu_ajuda)
    menu_ajuda.add_command(label="Sobre o programa…", command=sobre)

    # --- Frame principal ---
    frame = ttk.Frame(root, padding="12")
    frame.grid(column=0, row=0, sticky=tk.NSEW)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    var_texto = tk.StringVar()
    adivinhar = criar_callback_adivinhar(tokens, var_texto)

    ttk.Label(frame, text="Digite 2+ palavras:").grid(column=0, row=0, sticky=tk.W)
    entrada = ttk.Entry(frame, width=30, textvariable=var_texto)
    entrada.grid(column=1, row=0, sticky=tk.EW, padx=(8, 8))
    ttk.Button(frame, text="Analisar", command=adivinhar).grid(column=2, row=0)

    frame.columnconfigure(1, weight=1)

    for widget in frame.winfo_children():
        widget.grid_configure(pady=4)

    entrada.focus()
    root.bind("<Return>", adivinhar)

    root.mainloop()


if __name__ == "__main__":
    main()
