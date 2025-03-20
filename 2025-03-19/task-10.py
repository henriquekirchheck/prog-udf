#!python

km = float(input("Velocidade do carro (km/h): "))
multa = (km - 80) * 5
if multa > 0:
    print(f"Sua multa é de R${multa:.02f}")
