def binary(arr, num, low, high):
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] == num:
            return mid
        
        elif num > arr[mid]:
            low = mid+1
        
        else:
            high = mid -1
    
    return -1

arr1 =[3,4,5,6,7,8,9]
num1=4
low=0
high= len(arr1)-1

output = binary(arr1,num1,low,high)

if output != -1:
    print('Number is present at index', str(output))
else:
    print('Number not present!')




