#!python

animes = {
    "Naruto": 220,
    "Jujutsu Kaisen": 47,
    "Dragon Ball Z": 291,
    "Death Note": 37,
    "Fullmetal Alchemist": 64,
    "Evangelion": 26,
    "Berserk": 25,
    "Code Geass": 50,
    "Akame ga Kill!": 24,
    "Elfen Lied": 13
}

total = sum(animes.values())
porcentage = list(map(lambda x: (x[0], x[1] / total), animes.items()))
porcentage.sort(key=lambda x: x[1], reverse=True)

print(f"Total de eps {total}")
print("Porcentagem do total por serie")
for (name, value) in porcentage:
    print(f"{name}: {value * 100:.2f}%")
