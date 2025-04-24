#!python

alunos = {
    "Alice": 8.5,
    "Bruno": 7.8,
    "Carla": 9.2,
    "Diego": 6.9,
    "Eva": 8.0,
    "Fernando": 7.5,
    "Gabriela": 9.0,
    "Henrique": 6.7,
    "Isabela": 8.3,
    "João": 7.2,
}

print(f"Numero de alunos: {len(alunos)}")
print(f"Alguem tirou nota zero? {not any(alunos.values())}")
print(f"Maior nota: {max(alunos.values())}")
print(f"Menor nota: {min(alunos.values())}")
