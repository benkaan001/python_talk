'''
    \d matches any digits ---> [0-9]
    \D is the opposite of \d --> [^0-9]
    
'''
import re 


print(re.search('\d', 'foo123bar'))     # <re.Match object; span=(3, 4), match='1'>
print(re.search('[0-9]', 'foo123bar'))  # <re.Match object; span=(3, 4), match='1'>


print(re.search('\D', '12345_abc'))      # <re.Match object; span=(5, 6), match='_'>
print(re.search('[^0-9]', '123445_abc')) # <re.Match object; span=(5, 6), match='_'>
