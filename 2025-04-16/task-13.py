#!python

people: list[tuple[str, int]] = []
while (name := input("Digite o nome (vazio para parar): ")) != "":
    age = int(input("Digite a idade: "))
    people.append((name, age))

print(max(people, key=lambda x: x[1])[0])
