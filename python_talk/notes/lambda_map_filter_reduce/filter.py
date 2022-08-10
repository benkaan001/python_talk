import statistics
# task -> list the values that are above the mean
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# find the mean value
avg = statistics.mean(data)

# filter(func OR None, seq)

# filter returns a filter object that we need to unpack
filter_obj = filter(lambda x: x > avg, data)
print(list(filter_obj))  # [2.7, 4.1, 4.3]   

# data that needs clean up
countries = [0.0, 0j, (), "Argentina", {}, "Ecuador", "Mexico", "", "Peru", "", "", False, []]

# if function is None, filter returns the items that are true
filtered = list(filter(None,countries))   
# ['Argentina', 'Ecuador', 'Mexico', 'Peru']

# filter countries that contain 'a'
contains_a = list(filter(lambda x: 'a' in str(x), filtered))
# ['Argentina', 'Ecuador'] 

# filter by length
length_above_5 = list(filter(lambda x: len(str(x)) > 5, filtered))
# ['Argentina', 'Ecuador', 'Mexico']