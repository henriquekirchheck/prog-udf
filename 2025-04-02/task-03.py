#!python

from random import randint

sum = 0
while sum < 1000:
    rand = randint(0, 100)
    sum += rand
    print(rand)
