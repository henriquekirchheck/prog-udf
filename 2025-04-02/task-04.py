#!python

while input("Digite seu nome: ") != "Joe":
    pass

tries = 0
while input("Digite sua senha: ") != "swordfish":
    print("Incorreta")
    tries += 1
    if tries == 3:
        print("Encerrado")
        break
