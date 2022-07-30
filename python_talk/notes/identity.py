# IDENTITY OPERATORS checks if both identifiers refer to the same object

# immutablity of the object plays a key role




# IMMUTABLE

a = 10
b = 10
print(a is b) # True

# AVOID USING 'is' to compare values; ONLY use it for object comparison
c = 10.0
print(type(c)) # "<class float>"
print(c is a) # False


# MUTABLE

list1 = []
list2 = []
list3 = list1
print(list1 is list2) # False

# both lists are pointing to the same object
print(list3 is list1) # True



""" Equality operator (==) compares the values of both operands """


print(list1 == list2) # True

list4 = [(9+1)]

print(list4[0] is a) # True 

