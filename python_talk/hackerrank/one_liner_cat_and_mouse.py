'''
Two cats and a mouse are at various positions on a line. 
You will be given their starting positions. 
Your task is to determine which cat will reach the mouse first, 
assuming the mouse does not move and the cats travel at equal speed. 
If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.
'''
import math
def cat_and_mouse(x,y,z):
    
    dist_x = math.fabs(x-z)
    dist_y = math.fabs(y-z)
    return 'Cat A' if dist_x < dist_y else 'Cat B' if dist_y < dist_x else 'Mouse C'


output1 = cat_and_mouse(1, 2, 3)
output2 = cat_and_mouse(1, 3, 2)
print(output1, output2)