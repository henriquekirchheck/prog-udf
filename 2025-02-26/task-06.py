#!python

from math import factorial
import sys
import time

sys.set_int_max_str_digits(2147483647)

num = int(input("Digite um numero: "))


t1 = time.time()
print(factorial(num))
t2 = time.time()
print(t2 - t1)

t1 = time.time()
x = 1
for i in range(2, num + 1):
    x *= i
print(x)
t2 = time.time()
print(t2 - t1)
