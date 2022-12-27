'''
Greedly replace the higher elements

i.e if the input is [3,2,1,4,5] and k=1 then we swap 5 with 3 and the output = [5,2,1,4,3]

'''

def find_largest_permutation(arr, k):
    i=0
    max=len(arr)
    dic={x: i for i,x in enumerate(arr)}
    # dic = {3:0, 2:1, 1:2, 4:3, 5:4}
    
    # while k exists/ k>0 and len(arr)>0
    while k and i < len(arr):
        j = dic[max]
        if i ==j:
            pass
        else:
            #swap is required so decrease k by 1
            k-=1
            #swap the values in the array
            arr[i],arr[j] = arr[j], arr[i]
            #also update the dictionary 
            dic[arr[i]], dic[arr[j]] = dic[arr[j]], dic[arr[i]]
        
        i+=1
        max-=1

k=3
arr1=[3,2,1,4,5]
find_largest_permutation(arr1,k)