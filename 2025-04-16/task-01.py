#!python

from random import random
from time import sleep


is_raining = False
has_umbrella = False

if is_raining:
    print("Go outside")
    exit()

if has_umbrella:
    print("Go outside")
    exit()

while is_raining:
    print("Wait a while")
    sleep(2)
    if random() < 0.2:
        is_raining = False

print("Go outside")
