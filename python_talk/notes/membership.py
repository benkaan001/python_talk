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



# EXAMPLE

# notice that pyhon is assigned to a list containing a string 'cool'. 
# result is checking if python contains another list inside that has a string 'cool' 

python = ['cool']
print(python) # ['cool']
result = python in python
print(result) # False
true_result = python in [python] # True

scala = ['not as cool']
nested_scala = [['not as cool']]
result = scala in nested_scala
print(result) # True


 
