
numbers = [3, 5, 2, 4, 7, 1]

      
min_value, *rest = sorted(numbers)

print(min_value) # 1

print(rest)      # [2, 3, 4, 5, 7]

# Note that numbers have not changed since we used sorted() instead of sort()
print(numbers)   # [3, 5, 2, 4, 7, 1]

*rest, max_value = sorted(numbers)
print(max_value) # 7

print(rest)      # [1, 2, 3, 4, 5]