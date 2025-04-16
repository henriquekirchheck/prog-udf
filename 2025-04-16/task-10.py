#!python

nums: list[int] = []
while (num := int(input("Digite o numero (negativo para parar): "))) >= 0:
    nums.append(num)
par = list(filter(lambda x: x & 1 == 0, nums))
impar = list(filter(lambda x: x & 1 == 1, nums))

print(f"Par: {len(par) / len(nums) * 100}%")
print(f"Impar: {len(impar) / len(nums) * 100}%")
