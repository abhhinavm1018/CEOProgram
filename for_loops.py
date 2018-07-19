"""
title: for_loops
author: Abhinav Mugunda
date: 7/19/18 11:32 AM
"""

def create_string():
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
    ret = ''
    for num in letters:
        ret += num
    return ret


if __name__ == '__main__':
        print(create_string())


def caesar_cipher(encrypted):
    cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
                  'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
                  'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
    decryption = ""
    for num in range(0, len(encrypted)):
        decrypt_letter = encrypted[num]
        oddballs = (" ", "?", "!")
        if decrypt_letter in oddballs:
            decryption += decrypt_letter
        else:
            key_answer = cipher_key[decrypt_letter]
            decryption += key_answer
    return decryption


if __name__ == '__main__':
    print(caesar_cipher("pnrfne pvcure? v zhpu cersre pnrfne fnynq!"))


def matches (ticket, winners):
    ret_matches = 0
    for num in range(0,len(ticket)):
        if int(ticket[num]) == int(winners[num]):
            ret_matches = ret_matches + 1
    return ret_matches


def fill_ticket():
    ticket = []
    for num in range (0,5):
        guess = input("Enter a number: ")
        ticket += guess
    return ticket


# guesses = fill_ticket()
#
# winners = [1, 2, 3, 4, 5]
# print(matches(guesses, winners))


def short_hand(short):
    if "and" in short.lower():
        short = short.replace("and", "&")
    if "too" in short.lower():
        short = short.replace("too", "2")
    if "you" in short.lower():
        short = short.replace("you", "U")
        short = short.replace("You", "U")
    if "for" in short.lower():
        short = short.replace("for", "4")
    vowels = "aeiouAEIO"
    for letters in short:
        if letters in vowels:
            short = short.replace(letters, "")
    return short


print(short_hand("Thank you for that! You are too sweet and kind!"))