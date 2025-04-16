#!python

while True:
    if input("Who are you? ") != "Joe":
        continue
    if input("Hello, Joe. What is the password? (It is a fish) ") != "swordfish":
        continue
    break
print("Access granted.")
