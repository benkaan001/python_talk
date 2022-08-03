from itertools import permutations

a = [1,2,3]

# returns an object
perm = permutations(a)
# '<itertools.permutations object at 0x10a581e00>'


# that we can unpack by converting it into a list
perm_list = list(perm)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 



# optionally we can pass length argument
short_perm = list(permutations(a, 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
