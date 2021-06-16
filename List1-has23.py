# https://codingbat.com/prob/p177892
# List-1 > has23
# Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
    if nums[0] == 2 or nums[1] == 2:
        return True
    elif nums[0] == 3 or nums[1] == 3:
        return True
    else:
        return False
