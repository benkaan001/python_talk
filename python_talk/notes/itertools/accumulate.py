from itertools import accumulate
import operator
""" by default calculate additon
    in order to perform other aritmetic operations
    we need to import operator 
"""
a = list(range(1,5))
# [1,2,3,4]

# returns the iterable object
acc = accumulate(a)
# '<itertools.accumulate object at 0x10bb51c80>'

# which we unpack ...
accumulated = list(acc)
# [1, 3, 6, 10]


# we need to pass in the optional `func` arg to perform different calculations
mutli_accumulator = list(accumulate(a, func=operator.mul))
# [1, 2, 6, 24]