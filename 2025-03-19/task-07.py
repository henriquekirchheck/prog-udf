#!python

from collections import Counter

for key, i in Counter(input("Digite algo: ").upper()).items():
    print(f"{key}: {i}")
