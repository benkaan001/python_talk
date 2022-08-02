from collections import deque
d = deque()


# add items to the deque

d.append(1)
d.append(2)
d.append(3)
# deque([1, 2, 3])


# append to the left
d.appendleft(4) 
# deque([4, 1, 2, 3]) 


# remove the last element
d.pop()
# deque([4, 1, 2])


# remove the first element
d.popleft()
# deque([1, 2]) 


# remove all 
d.clear()
# deque([]) 


# add multiple elements to the end
d.extend(range(1,11))
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 


# add multiple elements from the beginning
# notice the order of a,b,c
d.extendleft(['a','b','c'])
# deque(['c', 'b', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# rotate all elements to the right
d.rotate()
# deque([10, 'c', 'b', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9])


# rotate all elemnts to the left
d.rotate(-1)
# deque(['b', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'c']) 







