from random import randint
x = randint(1,6)
guess = int(input("Guess the number: "))
if guess==x:
    print(True)  