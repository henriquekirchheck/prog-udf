#!python

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print(f"O maior é {[n1, n2][n1 < n2]}")
