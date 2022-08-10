
def add10(x): return x + 10
add10(5) # 15

# lambda 
add10 = lambda x: x + 10
print(add10(5)) # 15

# multiplication
mult = lambda x,y: x*y 
print(mult(2,7)) # 14

# with lists
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# sort by x
points2D_sorted_by_x = sorted(points2D)  
# [(1, 2), (5, -1), (10, 4), (15, 1)] 


# sort by y 
points2D_sorted_by_y = sorted(points2D, key=lambda x: x[1])
# [(5, -1), (15, 1), (1, 2), (10, 4)] 

# func version
def sort_by_y(pair): return pair[1]
points2D_sorted_by_y = sorted(points2D, key=sort_by_y)
# [(5, -1), (15, 1), (1, 2), (10, 4)] 



# map(func, seq)
a = [1,2,3,4,5]
a_doubled = list(map(lambda x: x*2, a)) # [2, 4, 6, 8, 10]
# cleaner approach
doubled = [num*2 for num in a]


# filter(func, seq)
odd_numbers = list(filter(lambda a: a%2 != 0, a)) # [1, 3, 5] 
# cleaner approach 
odd_nums = [num for num in a if num%2 != 0] # [1, 3, 5]
 
 
# reduce(func, seq)
# must import 
from functools import reduce
product = reduce(lambda x,y: x*y, a) # 120
# cleaner approach
prod =1
for num in a:
    prod*=num
print(prod) # 120






