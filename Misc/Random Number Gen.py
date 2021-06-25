import random

NumberLength = 6
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    RNO = "".join(random.choice(Number) for i in range(NumberLength))
    print(RNO)
    input("Press ENTER To Generate A New Number\n")
