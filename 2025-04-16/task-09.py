#!python

notas: list[int] = []
while (nota := int(input("Digite a nota (negativo para parar): "))) >= 0:
    notas.append(nota)
print(f"A media é {sum(notas) / len(notas)}")
