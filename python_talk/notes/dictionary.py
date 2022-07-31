words = ["one"]
# append for one item, extend for inserting sequence
words.extend(["two", "three", "four"])

words_in_tuple = [(index, word) for index, word in enumerate(words,1)]
# [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')] 

# create a dictionary from tuple
word_dict = {key:value for key,value in words_in_tuple}
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'} 

#or by invoking the built-in dict()

word_dict_too = dict(words_in_tuple)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'} 

# sort
sorted_keys = sorted(word_dict)
#[1, 2, 3, 4] 

# check membership
has_one = 1 in word_dict 
# true

# create a dictionary
calories = dict(burger=1000, apple=100, pizza=1200)
# {'burger': 1000, 'apple': 100, 'pizza': 1200} 

