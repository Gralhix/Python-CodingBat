# https://codingbat.com/prob/p107010
# String-1 > first_half
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


def first_half(str):
    return str[0:len(str)//2]
