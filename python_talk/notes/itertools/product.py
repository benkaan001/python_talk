from itertools import product

a = [1,2]
b = [3,4]

# perfroms cartesian multiplication 
prod_obj = product(a,b)
# '<itertools.product object at 0x10bd04a00>'

# we need to unpack the product object by converting it into a list
listy =list(prod_obj)

# [(1, 3), (1, 4), (2, 3), (2, 4)] 


# we can pass optional repeat value to repeat the cartesian multiplication
list1 = ["a","b"]
list2 = ["z"]
repeating_prod_obj = product(list1,list2, repeat=2)

repeating_list = list(repeating_prod_obj)
# [('a', 'z', 'a', 'z'), ('a', 'z', 'b', 'z'), 
# ('b', 'z', 'a', 'z'), ('b', 'z', 'b', 'z')]
