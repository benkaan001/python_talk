from collections import Counter
""" Counter takes an iterable ie string,list, etc"""

stringy = "aaabaaabbbbcccd"

str_counter = Counter(stringy) 
# Counter({'a': 6, 'b': 5, 'c': 3, 'd': 1})

# get keys
str_counter.keys() 
# dict_keys(['a', 'b', 'c', 'd']) 

# get values
str_counter.values() 
# dict_values([6, 5, 3, 1]) 

# get elements
elements = str_counter.elements()
# returns an object '<itertools.chain object at 0x109c057f0>'
# which we can convert into a list
counter_list = list(elements)
# ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd']


# find the most common element (number of elements)
str_counter.most_common(1)
# [('a', 6)]


# as seen above, it returns a tuple nested inside a list 
element = str_counter.most_common(1)[0][0] # a
