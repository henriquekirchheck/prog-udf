#!python

def palindrome(val: str) -> bool:
    assert(" " not in val)
    return val == val[::-1]

print(palindrome(input("Digite: ")))
