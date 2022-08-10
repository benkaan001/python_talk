import math

# map(func, seq)

radii = [2, 5, 7.1, 0.3, 10]

def area(r):
    """Area of a cicle with radius 'r'."""
    return math.pi * (r**2)

# map returns a map object that we can unpack using list
map_obj = map(area,radii)   # <map object at 0x108f73580>

print(list(map_obj)) # [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793]


# convert the temps given in c to f 

temps =[("Berlin", 29), ("Stockholm", 25), ("Oslo", 22), ("Tokyo", 30), ("Buenos Aires", 19)]

c_to_f = lambda x: (x[0], x[1]* 9/5 + 32)

# map returns a map object that we can unpack using list
map_obj = map(c_to_f, temps)
map_list = list(map_obj)

print(map_list)   # [('Berlin', 84.2), ('Stockholm', 77.0), ('Oslo', 71.6), ('Tokyo', 86.0), ('Buenos Aires', 66.2)]



