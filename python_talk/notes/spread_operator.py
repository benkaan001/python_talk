
numbers = [3, 5, 2, 4, 7, 1]

      
min_value, *rest = sorted(numbers)

print(min_value) # 1

print(rest)      # [2, 3, 4, 5, 7]

# Note that numbers have not changed since we used sorted() instead of sort()
print(numbers)   # [3, 5, 2, 4, 7, 1]

*rest, max_value = sorted(numbers)
print(max_value) # 7

print(rest)      # [1, 2, 3, 4, 5]


# dictionary literal **
concert_date = {'year': 2020, 'month': 1, 'day': 1}
artist_info = { 'artist': 'Beethoven', 'title': 'Symphonhy No 5'}
full_concert_info = {**concert_date, **artist_info}
# {'year': 2020, 'month': 1, 'day': 1, 'artist': 'Beethoven', 'title': 'Symphonhy No 5'}