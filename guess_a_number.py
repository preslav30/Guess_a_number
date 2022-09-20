import random


def guess_number(guess):
    number_chosen_by_computer = random.randint(1, 100)
    print(number_chosen_by_computer)
    while True:
        if guess == number_chosen_by_computer:
            return "You have guessed the number!"
        elif guess < number_chosen_by_computer:
            print("Too low. Guess again!")
        elif guess > number_chosen_by_computer:
            print("Too high. Guess again!")
        guess = int(input())


print(guess_number(guess=(input("Guess a number from 1 to 100:\n"))))
