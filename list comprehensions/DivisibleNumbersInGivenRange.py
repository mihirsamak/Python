# To check total numbers divisible by a given number for a given range:
# function will return a single number representing the total numbers
# for e.g. if range is 20 - 43 (both numbers inclusive) and number is 7, function will return 4

import operator
from itertools import repeat


def divisible(a, b, num):
    if num == 0:  # Check if number is zero
        raise ZeroDivisionError
    if a > b:  # Check if the start number of range is larger than end number
        a, b = b, a
    count = list(filter(lambda x: x == 0, (map(operator.mod, range(a, b + 1), repeat(num))))).count(0)
    print(list(filter(lambda x: x == 0, (map(operator.mod, range(a, b + 1), repeat(num))))))
    return count

# --------------- Explanation ---------------------------------------
# map(operator.mod, range(a, b + 1), repeat(num))) will take numbers in range a and b+1
# And the number and use modulus operator on them

# repeat(num) will repeat the dividing number as many times as there are numbers in the range

# (filter(lambda x: x == 0, (map(operator.mod, range(a, b + 1), repeat(num))))) will filter out
# all the numbers that have the result 0 from the modulus operator i.e. those which are completely divided.

# count(0) will return the count of elements that have value 0
