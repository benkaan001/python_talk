l=[]         # False
l=[[]]       # True
l =[None]    # True
l = [False]  # True

if l:
    print(True)
else:
    print(False)
    
"""
    Boolean Conversion 
    
    trivial values   ->  False
    non-trivial      ->  True

"""

# only 0 is converted to False, every other number is True

bool(-3.83) #True


# except empty string, all string values evaluate to True

bool("") # False
bool(" ") # True 


""" We can convert booleans to other objects """

str(True)     # 'True'
str(False)    # 'False'

int(True)     # 1

5 + True      # 6
