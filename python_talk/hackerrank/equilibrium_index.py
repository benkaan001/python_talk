"""

Find and return the equilibrium_index index of an array. 
Equilibrium index of an array is an index i such that 
the sum of elements at indices less than i is equal to 
the sum of elements at indices greater than i.

Element at index i is not included in either part.
If more than one equilibrium_index index is present, 
you need to return the first one. 
And return -1 if no equilibrium_index index is present.

Sample Input : -7 1 5 2 -4 3 0
Sample Output : 3 
"""

def equilibrium_index(arr): 
  
    # initalize right_sum to sum of the array
    right_sum = sum(arr) 
    
    # initialize left sum to zero 
    left_sum = 0
    
    for i, num in enumerate(arr): 
          
        # deduct num from right_sum for each move in i
        right_sum -= num 
          
        if left_sum == right_sum: 
            return i 
        
        # add num to left_sum for each move in i
        left_sum += num 
       
    # if no equilibrium_index index found, then return -1 
    return -1

input_str= "-7, 1, 5, 2, -4, 3, 0"
arr = [int(i) for i in input_str.split(",")]
output = equilibrium_index(arr) # 3
print(f"equilibrium value is {arr[output]}") # 'equilibrium value is 2'


"""
right_sum = 0 


left_sum = 0 

i = 0 | num = -7 | i = 1 | num = 1 | i = 2 | num = 5 | i = 3 | num = 2 
                 |                 |                 | 
                 |                 |                 | 
right_sum = 7    | right_sum = 6   | right_sum = 1   | right_sum = -1 
                 |                 |                 | 
                 |                 |                 | 
                 |                 |                 | return 3 
left_sum = -7    | left_sum = -6   | left_sum = -1   | 


"""