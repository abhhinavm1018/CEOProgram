"""
title: strings
author: Abhinav Mugunda
date: 7/18/18 2:45 PM
"""


def how_eligible(essay):
    count = 0
    if "!" in essay:
        count += 1
    if "?" in essay:
        count += 1
    if "," in essay:
        count += 1
    if '"' in essay:
        count += 1
    return count


if __name__ == '__main__':
    print(how_eligible('This? "Yes." No, not really!'))
    print(how_eligible('Really, not a compound sentence.'))


