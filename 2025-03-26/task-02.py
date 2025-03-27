#!python

from random import randint


nums = list(map(lambda _: randint(0, 1000), range(0, 10)))
for num in nums:
    print("bows" if num % 10 == 0 else num)
print(f"Soma: {sum(nums)}")
print(f"Min: {min(nums)}")
print(f"Max: {max(nums)}")
