'''
    A regex is a special sequence of characters that
    defines a pattern for complex string-matching functionality.
'''

s = 'foo123bar'

print('123' in s) # True

print(s.find('123'))  # 3
print(s.index('123')) # 3

"""
    Regex comes in for help when we need to more elaborate searches
    such as any three consecutive decimnal digit charactrers in a group
    of strings 'foo123bar', '987baz', 'bar345baz', etc.
    
    re.search(<regex>,<string>) 
        
        returns a match object 

"""

import re 

match_obj = re.search('123', s)
print(match_obj) # <re.Match object; span=(3, 6), match='123'>

# span = (3,6) indicates the portion of the string in which the match was found
# just as in the slice operation
span_chars = s[3:6] # 123

