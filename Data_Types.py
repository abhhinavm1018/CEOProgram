"""
title: Data_Types
author: Abhinav Mugunda
date: 7/18/18 10:31 AM
"""


def mean(a, b, c):
    """Finding the average of 3 numbers"""
    return (a + b + c) / 3


if __name__ == "__main__":
    print(mean(4, 7, 8))


def distance_formula (x1, y1, x2, y2):
    """Finding the distance between 2 points given x and y values"""
    return ((x2 - x1)**2 + (y2 - y1)**2)**.5


if __name__ == "__main__":
    print(distance_formula(1, 2, 5, 6))

