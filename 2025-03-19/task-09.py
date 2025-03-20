#!python

a = float(input("Digite coeficiente a: "))
b = float(input("Digite coeficiente b: "))
c = float(input("Digite coeficiente c: "))

delta = b * b - 4 * a * c

print("reais" if delta >= 0 else "complexas")
