'''
explanation 

step1 => choose the three integers where the difference is minimum
step2 => calculate max(3 integers) and min(3 integers)
step3 => return the difference
difference => max(10,20,30) - min(10,20,30) = 30-10 => 20

sorted_array= [10, 20, 30, 100, 200, 300, 1000]
maxNum =1000
difference => 
i=0 => 20
i=1 => 80
i=2 => 170
i=3 => 200
i=4 => 800


'''

def max_min(arr,k):
    arr.sort()
    max_num=arr[len(arr)-1]
    
    for i in range(len(arr)-k+1):
        difference =arr[i+k-1] - arr[i]
        if(difference<max_num):
            max_num=difference
    
    return max_num

    
    
k=3
arr=[10,100,300,200,1000,20,30]
max_min(arr, k)