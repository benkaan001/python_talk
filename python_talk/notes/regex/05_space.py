'''
    \s matches any whitespace
    
    Unlike the dot wildcard metacharacter, \s matches a newline character
    
'''

import re 

# Unlike the dot wildcard metacharacter, \s matches a newline character
print(re.search('\s', 'foo\nbar baz')) # <re.Match object; span=(3, 4), match='\n'>


# \S is the opposite 
print(re.search('\S', ' \n \n    '))  # None
print(re.search('\S', '\mnl ')) # <re.Match object; span=(0, 1), match='\\'>

# character class sequences \w, \W, \d, \D, \s, and \S can appear inside []
print(re.search('[\d\w\s]', '---3---'))      # <re.Match object; span=(3, 4), match='3'>
print(re.search('[\d \w\s]', '---a---'))      # <re.Match object; span=(3, 4), match='3'>
print(re.search('[ \d \w \s ]', '--- ---'))  # <re.Match object; span=(3, 4), match='3'>

# pay attention to excess code as [\w\s] == [\w\d\s]
print(re.search('[\w\s]', '---3---')) # <re.Match object; span=(3, 4), match='3'>