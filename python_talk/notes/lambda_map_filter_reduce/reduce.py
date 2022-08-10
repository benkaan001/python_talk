"""
    ->  Apply a function (or callable) to the first two items in an iterable 
        and generate a partial result.
        
    ->  Use that partial result, together with the third item in the iterable, 
        to generate another partial result.
        
    ->  Repeat the process until the iterable is exhausted 
        and then return a single cumulative value.
"""


# As of Python 3.0, reduce got downgraded to functools and is no longer a built-in module
from functools import reduce

# Multiply all numbers in a given list

lst = [2, 10, 5, 3, 7, 6 ]

multiplier = lambda x,y: x*y
reduced = reduce(multiplier, lst)
print(reduced) # 12600
# (2, 10 => 20) | (20, 5 => 100) | (100, 3 => 300) | (300, 7 => 2100) | (2100, 6 => 12600) 


# reduce has an optional third argument <INITIALIZER>
print(reduce(multiplier,lst, 0.1)) # 1260.0
# (0.1, 2 => 0.2) | (0.2, 10 => 2.0) | (2.0, 5 => 10.0) |
# (10.0, 3 => 30.0) | (30.0, 7 => 210.0) | (210.0, 6 => 1260.0)


# A simple for loop is more readable though reduce() provides better performance
product = 1
for num in lst:
    product*=num

print(product) # 12600

""" SKY IS THE LIMIT IN TERMS OF ADDITIONAL TOOLS TO ACHIEVE THE SAME RESULT """
# with built in prod()

from math import prod
# prod(seq)
print(prod(lst)) # 12600

# instead of user-defined lambda we can also take advantage of operator module
from operator import mul
print(reduce(mul,lst)) # 12600
