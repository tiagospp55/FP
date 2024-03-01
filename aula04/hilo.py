# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    flag = False

    while not flag:
        guess = int(input("Enter your guess: "))
        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            print("You got it!")
            flag = True

    print("Game over!")


main()
