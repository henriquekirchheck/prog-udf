#!python

from random import randint

sum = 0
while (n := randint(0, 9)) != 0:
    sum += n
print(sum)
