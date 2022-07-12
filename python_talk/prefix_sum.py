'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

def running_sum(arr):
    
    for i in range(1,len(arr)):
        arr[i] = arr[i]+arr[i-1]
    
    return arr;
    

arr = [3,1,2,10,1]

running_sum(arr) # [3, 4, 6, 16, 17]
