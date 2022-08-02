# any Python object capable of returning its members one at a time

string = "I have an idea!"
string_list = list(string)
# ['I', ' ', 'h', 'a', 'v', 'e', ' ', 'a', 'n', ' ', 'i', 'd', 'e', 'a', '!'] 


total_bill = sum(range(101)) 
# 5050

sorted_string = sorted(string)
# [' ', ' ', ' ', '!', 'I', 'a', 'a', 'a', 'd', 'e', 'e', 'h', 'i', 'n', 'v'] 

has_any_false = any((1, None, [], 0))