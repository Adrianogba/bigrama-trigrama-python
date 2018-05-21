import collections

#Para recursos não encontrados:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

# coding=utf-8

# Importação das Bibliotecas
from nltk.tokenize import sent_tokenize

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


with open('memorial_de_ayres.txt', 'r', encoding="utf-8") as myfile:
    data=myfile.read().replace('\n', ' ')
txtfiltrado = [w for w in word_tokenize(data.replace(',',' ').replace('.',' '))]

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



print(bigramas(txtfiltrado, ['a','casa']))

print(trigramas(txtfiltrado, ['podia','ser','um']))

