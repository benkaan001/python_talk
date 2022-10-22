
# For mutable objects, both the actual list and input list would point to the same object 
# AFTER the function is invoked.


def append_ten(input_list):
    
    print(f"Input list before function call: {input_list}") # [1,2,3]
    input_list.append(10)
    print(f"Input list after update inside function: {input_list}") # [1,2,3,10]
    
actual_list = [1,2,3]
print(f"Actual list before function call: {actual_list}") # [1,2,3]

append_ten(actual_list)
print(f"Actual list after function call: {actual_list}") # [1,2,3,10]

"""
Actual list before function call: [1, 2, 3]
Input list before function call: [1, 2, 3]
Input list after update inside function: [1, 2, 3, 10]
Actual list after function call: [1, 2, 3, 10]

"""