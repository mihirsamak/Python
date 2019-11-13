# To check if a list is permutation i.e. if it has all the positive integers till its Max value:
# i.e. if A = [1,5,7,3,6,4,2,9], it is not a permutation as '8' is missing while,
# if A = [1,5,7,3,6,4,2,9,10,8] is a permutation as all the numbers are present till its Max value '10'
# function will return True if list is permutation; else will return a tuple with False and the missing number
# for e.g. if A =[1,5,7,3,6,4,2,9] , function will return (False, 8)
# The list needs to have at least one positive integer in order to have a check

from itertools import filterfalse, count


def permutation(A):
    if not len(A):  # Check if the list is empty or not. Raise error if it is
        raise ValueError('List is empty')
    Max = max(A)
    if Max < 0:  # Check if the list has at least one positive integer
        raise ValueError('All elements in list are Negative')
    num = next(filterfalse(set(A).__contains__, count(1)))
    if num > Max: return True;
    return False, num

# --------------- Explanation ---------------------------------------
# (set(A).__contains__, count(1)) will convert the set A into a set to remove repetitive numbers and
# count will start a counter from 1. The set(A).__contains__ will check if the number is in the set
# filterfalse(set(A).__contains__, count(1)) will filter the false value, i.e. the first missing number
# 'next' will iterate the iterator until the first value, which will be the missing number

