#!python

from collections import Counter

palavra = input("Digite uma palavra: ")
if " " in palavra or any(map(lambda x: x.isnumeric(), palavra)):
    print("Erro input invalido")
    exit()
counter = Counter(map(lambda x: "v" if x in "aeiou" else "c", palavra))
print("Vogais: {v}\nConsoantes: {c}".format_map(counter))
