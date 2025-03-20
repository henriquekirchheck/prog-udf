#!python

while (num := int(input("Digite um numero (0 para parar): "))) != 0:
    print("Par" if num % 2 == 0 else "Impar")
