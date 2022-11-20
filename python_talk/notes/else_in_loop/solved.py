# What will this code output to the screen?
for i in range(5):
    print(i)
else:
    print('Done!')
    
"""
i = 0      | i = 1      | i = 2      | i = 3      | i = 4 
print('0') | print('1') | print('2') | print('3') | print('4') 

print('Done!')

"""


# Usage example
def contains_even_num(lst):
    for item in lst:
        if item % 2 == 0:
            print("List containes an even number")
            break 
    # Else executes only if break is never reached
    # and loop terminated after all iterations
    else:
        print("List does not contain any even numbers")

list1 = [1,2,3]
contains_even_num(list1)

"""
lst = [1, 2, 3] 
item = 1 | item = 2 
         | 
         | print('List containes an even number') 
         | 

"""

list2 = [1,3,5]
contains_even_num(list2)
"""
lst = [1, 3, 5] 
item = 1 | item = 3 | item = 5 
         |          | 
         |          | 
         |          | 
print('List does not contain any even numbers') 

"""
