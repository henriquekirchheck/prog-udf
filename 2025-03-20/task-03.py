#!python

num_sum = 0.0
while (num := float(input("Digite um numero positivo (0 para sair): "))) != 0:
    num_sum += num if num > 0 else 0
print(f"Soma {num_sum}")
