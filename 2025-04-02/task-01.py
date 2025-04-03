#!python

spam = int(1)

match spam:
    case 1:
        print("Hello")
    case 2:
        print("Howdy")
    case _:
        print("Greetings!")
