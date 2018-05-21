import collections
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

print("Este programa precisa do Python 3.x, podendo nao funcionar em outras versoes.")

#Para recursos não encontrados:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

# Importação das Bibliotecas
from nltk.tokenize import sent_tokenize

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


with open('memorial_de_ayres.txt', 'r', encoding="utf-8") as myfile:
    data_pt=myfile.read().replace('\n', ' ')
txtfiltrado_pt = [w for w in word_tokenize(data_pt.replace(',',' ').replace('.',' '))]

def sobre():
    messagebox.showinfo("Sobre o Preditor de Palavras:", "Este programa foi feito como nota para segunda avaliação de Inteligência Artificial, utilizando de bigramas e trigramas para adivinhar a mais provavel palavra dada uma sequencia de 2 ou 3 palavras.")


def adivinhar(*args):
    if(len(texto.get().split(" "))==2):
        n=bigramas(txtfiltrado_pt, texto.get().split(" "))
        if(len(n)==0):
            messagebox.showwarning("Erro", "Não há nenhuma sugestão dentro da base de dados.")
        else:
            print()
            messagebox.showwarning("Sucesso!!", "Sugestões para '"+texto.get()+"' são:\n\n"+', '.join(n))
    elif(len(texto.get().split(" "))==3):
        n=trigramas(txtfiltrado_pt, texto.get().split(" "))
        if(len(n)==0):
            messagebox.showwarning("Erro", "Não há nenhuma sugestão dentro da base de dados.")
        else:
            print()
            messagebox.showwarning("Sucesso!!", "Sugestões para '"+texto.get()+"' são:\n\n"+', '.join(n))
    else:
        messagebox.showerror("Erro:", "Apenas textos com 2 ou 3 palavras são aceitos.")


def bigramas(fonte, palavras):
    
    bigrams = []
    suggestions = []

    for i in range(0, len(fonte)):
        if (i == len(fonte)-1):
            break
        else:
            if(fonte[i].lower()==palavras[1].lower() and fonte[i-1].lower()==palavras[0].lower()):
                bigrams.append(fonte[i+1])

    counter = collections.Counter(bigrams)
    
    for i in range(0,len(counter.most_common())):
        if(i>=3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])
    
    return suggestions


def trigramas(fonte, palavras):

    trigrams = []
    suggestions = []

    for i in range(0, len(fonte)):
        if (i == len(fonte)-2):
            break
        else:
            if(fonte[i].lower()==palavras[2].lower()
               and fonte[i-1].lower()==palavras[1].lower()
               and fonte[i-2].lower()==palavras[0].lower()):
                
                trigrams.append(fonte[i+1])
 
    counter = collections.Counter(trigrams)
    
    for i in range(0,len(counter.most_common())):
        if(i>=3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])
    
    return suggestions



root = Tk()
root.title("Preditor de Palavras v0.3 - By Adriano Martins")
#root.wm_iconbitmap('Icon.ico')

menu = Menu(root)
root.config(menu=menu)

arquivo = Menu(menu)
menu.add_cascade(label="Arquivo", menu=arquivo)
arquivo.add_separator()
arquivo.add_command(label="Sair", command=quit)

ajuda = Menu(menu)
menu.add_cascade(label="Ajuda", menu=ajuda)
#ajuda.add_separator()
ajuda.add_command(label="Sobre o programa...", command=sobre)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

texto = StringVar()

ntexto = ttk.Entry(mainframe, width=15, textvariable=texto)
ntexto.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Digite um texto:\n(2 e 3 palavras)").grid(column=1, row=1, sticky=W)


ttk.Button(mainframe, text="Analisar", command=adivinhar).grid(column=3, row=1, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

ntexto.focus()
root.bind('<Return>', adivinhar)

root.mainloop()
