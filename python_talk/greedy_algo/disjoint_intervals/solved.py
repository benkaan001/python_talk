'''
The key advantage of getting the maximum number of disjointed Intervals
lies in the ending value of the inner pair. In other words, the lower the
ending value of the pair is the higher the chances of having a disjointed
interval. 
For this reason, we need to sort the array on the bases of the ending value
of the pairs, utilizing lambda.

sorted array = [[2,3], [1,4], [4,6], [8,9]]



'''

def disjoint_interval(arr):
    # arr = sorted(arr, key=lambda x: x[1])
    arr.sort(key=lambda x:x[1])
    
    #since we are gonna select the first pair we start the count at 1
    count =1
    
    [index0,index1] = arr[0]
    
    for [i,j] in arr:
        if i <= index0:
            pass
        else:
            index0,index1 = i,j
            count+=1
        
    return count
    


arr=[[1,4],[2,3],[4,6],[8,9]]
disjoint_interval(arr)






