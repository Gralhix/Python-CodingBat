# https://codingbat.com/prob/p165097
# Warmup-2 > front_times
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
    return (str[0:3]) * n  
