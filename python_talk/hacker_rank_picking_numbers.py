'''
Given an array of integers, find the longest subarray where the absolute difference 
between any two elements is less than or equal to 1.
Constraint 0<n<=100
a[n] --> n: item in array >=2
'''
def pickingNumbers(a):
    # Write your code here
  frequency = [0]*101
  max_count =0
  
  for i in range(len(a)):
      i_index = a[i]
      frequency[i_index]+=1
    
  for i in range(1, len(frequency)-1):
      if (frequency[i] + frequency[i+1] > max_count):
          max_count = frequency[i] + frequency[i+1]
  
  return max_count

    
                
    
    
        

sample = [1,1,2,2,4,4,5,5,5]  #5
sample = [9,9,9,14,14,14] #3
sample = [1,1,2,3,4,4,4,4,4,4,6,6,6,6,6,6,6,7] #8

print(pickingNumbers(sample))
