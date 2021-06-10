# https://codingbat.com/prob/p184816
# String-1 > first_two
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


def first_two(str):
    if len(str) < 2:
        return str
    return str[:2]