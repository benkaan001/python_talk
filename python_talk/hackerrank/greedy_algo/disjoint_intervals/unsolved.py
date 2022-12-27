'''

Given a set of N intervals, the task is to find the maximal set of mutually disjoint intervals. 
Two intervals [i, j] & [k, l] are said to be disjoint if they do not have any point in common. 

Input: intervals[][] = {{1, 4}, {2, 3}, {4, 6}, {8, 9}} 
Output: 
[2, 3] 
[4, 6] 
[8, 9] 
Intervals sorted w.r.t. end points = {{2, 3}, {1, 4}, {4, 6}, {8, 9}} 
Intervals [2, 3] and [1, 4] overlap. 
We must include [2, 3] because if [1, 4] is included then 
we cannot include [4, 6].
Input: intervals[][] = {{1, 9}, {2, 3}, {5, 7}} 
Output: 
[2, 3] 
[5, 7]  
'''
def disjoint_interval(arr):
    pass
    
  
    
    
arr=[[1,4],[2,3],[4,6],[8,9]]
disjoint_interval(arr)