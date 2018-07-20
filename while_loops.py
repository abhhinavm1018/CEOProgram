"""
title: while_loops
author: Abhinav Mugunda
date: 7/19/18 2:28 PM
"""


def credit_limit():
    initial_balance = int(input("Enter Account Balance: "))
    while initial_balance > 0:
        withdrawl = int(input("Enter Amount Spent: "))
        initial_balance -= withdrawl
        print("Amount left: " + str(initial_balance))
    print("All out of money!")


# if __name__ == '__main__':
#     credit_limit()


def pig_latin(pig):
    vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    if vowels.intersection(pig) == 0:
        return pig + "ay"
    if pig[0] in vowels:
        return pig + "yay"
    first_vowel_index = 0
    for num in range(0, len(pig)):
        if pig[num] in vowels:
            first_vowel_index = int(num);
            break
    return pig[0: first_vowel_index] + pig[first_vowel_index+1: len(pig)]


if __name__ == '__main__':
    print(pig_latin("hllelujah"))
