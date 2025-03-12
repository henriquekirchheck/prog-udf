#!python

n1 = float(input("Nota 1: "))
p1 = float(input("Nota 1 peso: "))
n2 = float(input("Nota 2: "))
p2 = float(input("Nota 2 peso: "))
n3 = float(input("Nota 3: "))
p3 = float(input("Nota 3 peso: "))

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(media)
