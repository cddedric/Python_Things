'''
oct 2018
author: Casey

Swaps case of all letters in the string 's' without using string's swapcase function
'''


def swap_case(s):
    #return s.swapcase() #built in python function that makes this too easy
    a=''
    for character in s:
        if character.isalpha():
            if character==character.upper():
                character=character.lower()
            else:
                character=character.upper()
        a+=character
    return a