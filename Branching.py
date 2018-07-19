"""
title: Branching
author: Abhinav Mugunda
date: 7/18/18 11:53 AM
"""


import random


def food_order(choice, menu):
    if choice in menu:
        return "Your order of " + choice + " will be ready soon"
    else:
        return "Your order of " + choice + " is not on the menu. Choose another option"


def guess_number(low, high):
    """Tell user if guess is out of range"""
    guess = int(input("Guess a number between " + str(low) + " and " + str(high) + ":"))
    if guess <= low:
        print("No, " + str(guess) + " is less than or equal to " + str(low))
    elif guess >= high:
        print("No, " + str(guess) + " is greater than or equal to " + str(high))
    else:
        print("Good! " + str(low) + " < " + str(guess) + " < " + str(high))


def guessing_game(low, high):
    count = 0
    correct = True
    target = random.randint(low, high)
    while correct:
        guess = int(input("Guess a number between " + str(low) + " and " + str(high) + ":"))
        if guess == target:
            count += 1
            print("Congratulations, you guessed my number in " + str(count) + " tries")
            correct = False;
        if guess < target:
            low = guess
            print("You were too low, try again")
            count += 1
        if guess > target:
            high = guess
            print("You were too high, try again")
            count += 1


# if __name__ == '__main__':
#     menu = ['pizza', 'salad', 'sushi', 'fajitas', 'omelets']
#     choice = input("Enter your choice of entrees: ")
#     print(food_order(choice, menu))


# if __name__ == '__main__':
#     guess_number(1, 100)


if __name__ == '__main__':
    guessing_game(1, 100)