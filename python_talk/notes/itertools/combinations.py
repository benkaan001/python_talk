from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]

# requires two args, iterable and length
comb = combinations(a, 2)
# '<itertools.combinations object at 0x10dc21900>'


# we can unpack the returned object by using list
# notice that it only returns non-repeating combos
combo = list(comb)
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]



# we need to import `this` to get ALL possible combinations
full_combo = list(combinations_with_replacement(a,2))
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), 
#  (3, 3), (3, 4), (4, 4)] 