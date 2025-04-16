#!python

nums: set[int] = set()
while (num := int(input("Digite o numero (negativo para parar): "))) >= 0:
    nums.add(num)
nums_list = list(nums)
print(nums_list)
