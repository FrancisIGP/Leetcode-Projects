# Guessing Game
import random

def guessingGame():
    attempts = int(3)
    random_num = random.randint(1, 20)

    print("\nWelcome to Guess the Number!\n")
    print("You only have 3 attempts to guess the number from 1-20!\n")

    while attempts != 0:
        try:
            guess = int(input(f"Enter your guess [Trials: {attempts}]: "))
            
            if guess == random_num: return "\nCongrats! You Won!"
            elif guess > random_num: print("Too High.\n")
            elif guess < random_num: print("Too Low.\n")
            attempts -= 1
        except:
            print("Invalid input!\n")
        
    return f"Sorry, you ran out of attempts. The correct number was {random_num}.\n"

print(guessingGame())