#!python

print("    ", end="")
for i in range(1, 11):
    print(f"{i:>3}", end=" ")
print(f"\n   ┌{'─'*39}")

for i in range(1, 11):
    print(f"{i:>2} │", end="")
    for j in range(1, 11):
        print(f"{i*j:>3}", end=" ")
    print()