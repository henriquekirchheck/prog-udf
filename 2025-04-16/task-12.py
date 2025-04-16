#!python

pessoas: set[tuple[float, float]] = set()
for i in range(1, 6):
    pessoas.add(
        (
            float(input(f"Digite a altura da {i}ª pessoa: ")),
            float(input(f"Digite o peso da {i}ª pessoa: ")),
        )
    )

if len(pessoas) < 5:
    print("Pelo menos duas pessoas tem a mesma altura e peso")
