import random
from art import logo




easy_guess = 10
hard_guess = 5
random_number = random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Hint: it is close to {random_number+25}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    for i in range(easy_guess):
        print(f"you have {easy_guess} attempts remaining to guess the number")
        num = int(input("Make a guess: "))
        easy_guess -=1
        if num>random_number:
            print("Too high")
        elif num<random_number:
            print("Too low")
        elif num == random_number:
            print(f"You got it! The answer was {random_number}")
            exit()
    print("You run out of guesses you lose")

elif difficulty == "hard":
    for i in range(hard_guess):
        print(f"you have {hard_guess} attempts remaining to guess the number")
        num = int(input("Make a guess: "))
        hard_guess-=1
        if num > random_number:
            print("Too high")
        elif num < random_number:
            print("Too low")
        elif num == random_number:
            print(f"You got it! The answer was {random_number}")
            exit()

    print("You run out of guesses you lose")


