# To check consecutive recurring numbers in a given list/Array:
# function will return a list of tuples with the number and its count paired together
# for e.g. if A = [2,0,1,2,3,3,3,3,0,1,1,1,1], function will return [(0, 2), (1, 5), (2, 2), (3, 4)]

from itertools import groupby

def consecutive(A):

    final_list = list(zip(set(A),[sum(1 for elements in group) for key, group in groupby(sorted(A))]))
    return final_list

