'''

Built-in mutable collections like list,dict, set can be copied by
calling their factory functions on an existing collection:

    new_dict = dict(original_dict)

...


A shallow copy means constructing a new collection object and then populating it 
with references to the child objects found in the original.
    A shallow copy is only one level deep. 
    The copying process does not recurse and 
    therefore won’t create copies of the child objects themselves.

A deep copy makes the copying process recursive. 
It first constructs a new collection object and then recursively 
populates it with copies of the child objects found in the original. 
    Deep copy walks the whole object tree to create a fully independent clone of 
    the original object and all of its children.
'''

original_list = [[1,2,3],[4,5,6],[7,8,9]] 
# create a shallow copy
shallow_copy = list(original_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

"""Confirm that shallow copy is a new and independent object"""
original_list.append(['original content']) 
print(original_list) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['original content']] 
print(shallow_copy)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

"""
Even though shallow_copy is an independent object, it still has reference to the child objects
stored in the original_list. 
Modifying one of the child objects in original list will be reflected in the shallow copy as well
"""
original_list[0][0] = 'potato'
print(original_list) # [['potato', 2, 3], [4, 5, 6], [7, 8, 9], ['original content']]
print(shallow_copy) # [['potato', 2, 3], [4, 5, 6], [7, 8, 9]]


# import copy module to use the deepcopy method
import copy 
original_list = [[1,2,3],[4,5,6],[7,8,9]] 
deep_copy = copy.deepcopy(original_list)

original_list.append(['original content'])
print(original_list) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['original content']]
print(deep_copy) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

original_list[0][0] = 'meow'
print(original_list) # [['meow', 2, 3], [4, 5, 6], [7, 8, 9], ['original content']]
print(deep_copy) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]




