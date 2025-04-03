#!python

for x in range(1, 11):
    print(x)

x = 0
while (x := x + 1) != 11:
    print(x)
