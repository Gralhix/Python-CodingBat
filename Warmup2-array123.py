# https://codingbat.com/prob/p193604
# Warmup-2 > array123
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


def array123(nums):
    for i in range(0,len(nums)):
        if nums[i:i+3] == [1, 2, 3]:
          return True
    return False

# Honestly I don't understand why the code works if the "return False" is in this indentation and not in the for loop
