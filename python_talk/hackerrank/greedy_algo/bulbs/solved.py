'''
N light bulbs are connected by a wire. 
Each bulb has a switch associated with it, however due to faulty wiring, 
a switch also changes the state of all the bulbs to the right of current bulb. 
Given an initial state of all bulbs, find the minimum number of switches 
you have to press to turn on all the bulbs. 
You can press the same switch multiple times. 
Note: 0 represents the bulb is off and 1 represents the bulb is on. 

SAMPLE 

Input :  [0 1 0 1]
Output : 4

Explanation :
    press switch 0 : [1 0 1 0]
    press switch 1 : [1 1 0 1]
    press switch 2 : [1 1 1 0]
    press switch 3 : [1 1 1 1]

Input : [1 0 0 0 0] 
Output : 1


??? What makes this greedy???
In each iteration we have to turn on the bulb if it is off even if 
(theoretically) this may not be the optimal solution, it is going to 
lead to a solution.

'''

def bulbs(arr):
    # this is the intial, as is case
    count=0
    flip= False
    
    for i in range(len(arr)):
        # a bulb is ON in two conditions
        # FIRST =>  the bulb is on and it is not supposed to be flipped
        if(arr[i] ==1 and flip is False):
            continue
        # SECOND => the bulb is off and it needs to be flipped
        if(arr[i] == 0 and flip is True):
            continue
        
        #at this point the bulb is off, so we have to turn it on
        # by incrementing the count and changing the flip state so
        # the state updates for the next iteration
        count+=1
        flip = not flip
    
    return count
        
arr =[0,1,0,1]
bulbs(arr)