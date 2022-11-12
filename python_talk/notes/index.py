
# index(item, start, end)

# issue index() return the first occurance of the target

str1 = "maybe pizza, maybe burger, maybe just some delicious meat ball sub"
target = "maybe"

index_list = [str1.index(x) for x in str1.split() if x == target ] # [0, 0, 0]

# solutions -> use ENUMERATE()

index_list = [x for x,y in enumerate(str1.split()) if y == target] # [0, 2, 4]