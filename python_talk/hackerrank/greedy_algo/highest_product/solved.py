'''

Steps to follow ===> 

1 => sort the array
2 => calculate potential highest value by multiplying the last three nums
3 => multiply the lowest two negative values and add the highest positive 
     value to the multiplication
4 => compare the two potential and return the higher value

Solution O(log n) due to sorting

VISUALIZATION 

sorted = [-20,-10,-3,5,6]
highest3 = 6 * 5 * -3 = -90
lowest3 = -20 * -10 * 6 = 1500


'''

def highestProduct(arr):
    
    arr = sorted(arr)
    
    highest3=arr[-1]*arr[-2]*arr[-3]
    lowest3 = arr[0]*arr[1]*arr[-1]
    
    return max(highest3,lowest3)
    


arr =[0,-1,10,7,5]
arr2=[1,2,3,4]
arr3 = [-10,-3,5,6,-20] #1200
highestProduct(arr3)