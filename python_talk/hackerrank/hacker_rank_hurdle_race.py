'''
A video player plays a game in which the character competes in a hurdle race. 
Hurdles are of varying heights, and the characters have a maximum height they can jump.
There is a magic potion they can take that will increase their maximum jump height 
by 1 unit for each dose. 
How many doses of the potion must the character take to be able to jump all of the hurdles.
If the character can already clear all of the hurdles, return 0 .

Example
height = [1,6,3,5,2]
k = 4
output = 6-4 =2

'''




def hurdleRace(k, height):
    # Write your code here
    height.sort()
    max = height[len(height) -1]
    
    if k > max:
        return 0
    else:
        return max-k

print(hurdleRace(4, [1,6,3,5,2])) # 2
print(hurdleRace(7, [2,5,4,5,2])) #0