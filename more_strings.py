"""
title: more_strings
author: Abhinav Mugunda
date: 7/19/18 9:27 AM
"""
import random

def is_this_a_letter():
        # Returns true is entered character is a letter, else false
        is_letter = input("Enter a character: ")
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if is_letter in alphabet:
                return True
        return False


def credentials_generator():
        # Creates credentials for the user based on given user information
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        birth_city = input("Enter Birth City: ")
        university = input("Enter Alma Mater University: ")
        relative = input("Enter a Relative's Name: ")
        friend = input("Enter a Friend's Name: ")
        employee_id = first_name[0:3] + last_name[len(last_name)-3:]
        user_name = birth_city[0:2] + university[len(university)-3:]
        password = relative[random.randint(0, len(relative)-1):] + friend[:random.randint(0,len(friend))]
        print("Employee ID: " + employee_id)
        print("User Name: " + user_name)
        print("Password: " + password)


# if __name__ == '__main__':
#         print(str(is_this_a_letter()))

if __name__ == '__main__':
    credentials_generator()
