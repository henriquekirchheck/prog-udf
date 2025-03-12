#!python
import time
import numpy as np

t1 = time.time()
print(100 * 101 / 2)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
print(sum(range(1, 101)))
t2 = time.time()
print(t2 - t1)

t1 = time.time()
print(np.sum(range(1, 101), dtype=np.int64))
t2 = time.time()
print(t2 - t1)

t1 = time.time()
x = 0
for i in range(1, 101):
    x += i
print(x)
t2 = time.time()
print(t2 - t1)
