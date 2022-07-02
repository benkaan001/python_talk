'''
 O (n log n) time complexity log n for sorting n for looping
'''

def minimum_absolute_difference(arr):
    
    arr.sort()

    min=arr[len(arr)-1]
    
    #min = MAXINT is another option
    
    for i in range (len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff <min:
            min=diff
            if diff==0:
                return 0
    return min
    



arr1 =[3,7,0]
arr2 = [-59,-36,-13,1,-53,-92,-2,-96,-54,75]


minimum_absolute_difference(arr2) #1
minimum_absolute_difference(arr1) #3
