x = 1
y = 1
z = 2
n = 3

"""
Print an array of all the permutations of x,y,z that do not add up to n
Print the list in lexicographic increasing order

Expected output:

[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]

"""

# loop version

mtx = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if not sum([i, j, k]) == n:
                mtx.append([i, j, k])

print(mtx)

# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

# comprehension

mtx_comprehension = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if not sum([i, j, k]) == n
]
print(mtx_comprehension)
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
