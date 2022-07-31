# checks if an object is in a sequence - lists, tuples, and strings


# tuple
has_five= 5 in (1,2,3) # False


# string
has_cat = "cat" in "the cat is in the hat" # True


# list 

# the list msut be an element of the list to be seen as a member
has_list = [1,2] in [None, [1,2], 0.8] # True

# cannot be a sub-sequence member 
has_list = [1,2] in [1,2,3] # False




 
