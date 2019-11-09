# To check consecutive recurring numbers in a given list/Array:
# function will return a list of tuples with the number and its count paired together
# for e.g. if A = [2,0,1,2,3,3,3,3,0,1,1,1,1], function will return [(0, 2), (1, 5), (2, 2), (3, 4)]

from itertools import groupby


def consecutive(A):
    if not len(A):  # Check if the list is empty or not. Raise error if it is
        raise ValueError('List is empty')
    final_list = list(zip(set(A), [sum(1 for elements in group) for key, group in groupby(sorted(A))]))
    return final_list

# --------------- Explanation ---------------------------------------
# groupby(sorted(A)) will group the sorted list of 'A' with 'key' being the number and
# 'group' being the total number of its occurrences

# sum(1 for elements in group) will add 1 for every element in 'group' i.e. give the sum of the occurrences

# [sum(1 for elements in group) for key, group in groupby(sorted(A))]
# will return a list consisting of only the occurrences

# Zip function will group the number and its occurrences as what is the desired output
