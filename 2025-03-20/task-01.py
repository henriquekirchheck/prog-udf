#!python

soma = 0.0
soma += float(input("Nota 1: "))
soma += float(input("Nota 2: "))

if soma / 2 >= 6:
    print("Aprovado")
    exit()

soma += float(input("Recuperação: "))

print(f"Media: {soma / 3:.02f}; {'Aprovado' if soma / 3 >= 6 else 'Reprovado'}")
