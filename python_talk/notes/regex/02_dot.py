'''
    The dot(.) metacharacter matches any character except a newline.
    This includes \n 
'''

import re 

s = 'foo123bar'
match_obj = re.search('1.3', s)
print(match_obj) # <re.Match object; span=(3, 6), match='123'>


# You are asking "Does s contain a '1', then any character except a newline, then a '3'?
# The answer is no in the cas of 'foo13bar'
s ='foo13bar'
print(re.search('1.3', s)) # None

print(re.search('foo.bar', 'fooxbar')) # <re.Match object; span=(0, 7), match='fooxbar'>
print(re.search('foo.bar', 'foo bar')) # <re.Match object; span=(0, 7), match='fooxbar'>
print(re.search('foo.bar', 'foobar'))   # None
print(re.search('foo.bar', 'foo\nbar')) # None