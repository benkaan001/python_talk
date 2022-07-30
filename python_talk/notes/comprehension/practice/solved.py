
floating = [2,3.75,.04,59.354,6,7.7777,8,9]
string1 = "No need for apology"
string2 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
vowels = ['a', 'e', 'i', 'o', 'u']
a = [1,2,3,4]
b = [2,3,4,5]
tuple1= "hi", 4, 8.99, 'apple', ('t','b','n')
string3 ="In 1984 there were 13 instances of a protest with over 1000 people attending"
digits=[0,1,2,3,4,5,6,7,8,9]



# remove floats from floating
no_float = [ num for num in floating if type(num) != float ]
# [2, 6, 8, 9] 


# find all numbers from 1-1000 that are divisible by 7
is_divisible_seven = [num for num in range(1,1000) if num % 7 == 0]
# [7, 14, 21, 28, 35, 42, 49, 56, 63,[625 chars] 952, 959, 966, 973, 980, 987, 994] 



# find all numbers from 1-100 that contain 3
contains_three = [num for num in range(1,100) for digit in str(num) if digit == '3' ]
# [3, 13, 23, 30, 31, 32, 33, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93] 



# count the number of spaces in string1
space_in_string1 = [letter for letter in string1 if letter == " "] 
# len(space_in_string1) --> 3


# create a list of unique consonants in string2
consonants = [letter for letter in set(string2.replace(" ", "")) if letter not in vowels]
# ['Y', 'k', 'h', 'm', 'w', 'n', 'y', 'g', 't', 'd', 'l', 'r', 's']


# create a list of words that are less than 4 letters in string2
four_or_less_lettered =[letter for letter in string2.split() if len(letter) <=4]
# ['Yaks', 'like', 'and', 'and', 'they', 'yuky', 'yams'] 


# find the common numbers in list a and b without using a tuple or set
common_nums = [num for num in a and b if num in a and b]
# [2, 3, 4] 


# create (index,value) list from tuple1
tuple_transform = [(index,value) for index,value in enumerate(tuple1)]
# [(0, 'hi'), (1, 4), (2, 8.99), (3, 'apple'), (4, ('t', 'b', 'n'))]


# extract the numeric values from string3 in the form of int
numeric = [int(word) for word in string3.split() if not word.isalpha()]
# [1984, 13, 1000] 


# given numbers in range 10, list words 'even' or 'odd' based on the number value
even_or_odd = ['even' if num %2 == 0 else 'odd' for num in range(1,11) ]
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even'] 


# create a tuple consisting of matching digits from list a and b - (2,2),(3,3),etc
pairs = [(x,y) for x in a for y in b if x==y]
# [(2, 2), (3, 3), (4, 4)] 


# using a nested list comprehension list numbers in range 1-21 that are divisible by any number
# between 10 and 20
nums = [num for num in range (1,21) for num2 in range(10,21) if num % num2 == 0]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20]

