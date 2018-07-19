"""
title: Lists
author: Abhinav Mugunda
date: 7/19/18 10:16 AM
"""
import random


def name_generator (first_list, last_list):
    first_name = random.choice(first_list)
    last_name = random.choice(last_list)
    return first_name + " " + last_name


def shake_ball():
    input("Ask a question: ")
    responses = ['Yes, definitely', 'As I see it, yes', 'Ask again later', 'Cannot predict now', "Don't count on it", 'Very Doubtful']
    return random.choice(responses)


# if __name__ == '__main__':
#     first_list = ["Joe", "Moe", "Bo", "LoLo", "Zo"]
#     last_list = ["Smith", "Rodriguez", "Hernandez", "Doe", "Phillips"]
#     print(name_generator(first_list, last_list))


if __name__ == '__main__':
    print(shake_ball())