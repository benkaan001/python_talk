letters = [
    "a",
    "a", "b",
    "a", "b", "c",
    "a", "b", "c", "d",
]

# COUNT ALL VALUES IN A LIST
len(letters)  # 10


# COUNT UNIQUE VALUES IN A LIST
len(set(letters)) #4


# COUNT INSTANCES OF A SPECIFIC VALUE
letters.count("a")  #4


# COUNT INSTANCES OF ALL UNIQUE VALUES
for letter in set(letters):
    print((letter, letters.count(letter)), end=" ") 
    # ('c', 2) ('b', 3) ('d', 1) ('a', 4) 


# COUNT USING DICTIONARY COMPREHENSION
letter_count_dict = {letter: letters.count(letter) for letter in letters}
# {'a': 4, 'b': 3, 'c': 2, 'd': 1}

# count all values in the list through the letter_count_dict dict
sum(letter_count_dict.values()) #10

# count unique values
len(letter_count_dict.keys()) #4

# count instances of a specific value
letter_count_dict["a"] #4
