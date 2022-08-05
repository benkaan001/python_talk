'''
Given two input strings, return the common characters.

If no common character found, return 'Not found'

Constraints :
- perform case-sensitive comparison
- ignore non-alphanumeric characters
- do not repeat if there is more than one same type of character
- do not use Set
- disgregard time complexity

'''

s1 = "Life is beautiful"
s2 = "Health is new wealth"


common = [x for x in set(s1)&set(s2)]

# ['t', ' ', 's', 'i', 'e', 'a', 'l'] 


# list comprehension

common_comprehensive = [x for x in set(s1) if x in set(s2)]