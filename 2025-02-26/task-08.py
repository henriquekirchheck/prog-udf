#!python

for n in range(1, 101):
    print([n, "Fiz", "Buz", "FizBuz"][(n % 3 == 0) + ((n % 5 == 0) * 2)])