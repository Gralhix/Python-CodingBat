# https://codingbat.com/prob/p127703
# String-1 > non_start
# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a, b):
    return a[1:] + b[1:]
