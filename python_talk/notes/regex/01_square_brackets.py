'''
    METACHARACTERS
    In regex, a set of characters specified in square brackets []
    makes up a 'character class'. This sequence matches any SINGLE 
    character that is in the class.
    
    * Other regex metacharacters such as *, +, | lose their special
      meanings inside a character class.
    
'''
import re

s = 'foo123bar'
match_obj = re.search('[0-9][0-9][0-9]', s)
print(match_obj) # <re.Match object; span=(3, 6), match='123'>


match_obj = re.search('[0-9][0-9][0-9]', '234baz')
print(match_obj) # <re.Match object; span=(0, 3), match='234'>


# On the other hand, a string that does not contain three consecutive digits won't match
s = '12foo34'
match_obj = re.search('[0-9][0-9][0-9]', s)
print(match_obj) # None

# you can enumerate the characters individually as in [artz] 
print(re.search('ba[artz]', 'foobarqux')) # <re.Match object; span=(3, 6), match='bar'>

# or you can search for a range of characters as in [a-z] all inclusive
print(re.search('[a-z]', 'FOObar')) # <re.Match object; span=(3, 4), match='b'>

# notice how [0-9][0-9] matches only the first two consequtive numbers
print(re.search('[0-9][0-9]', 'foobar01234')) # <re.Match object; span=(6, 8), match='01

# [0-9a-fA-F] matches the first HEXADECIMAL digit character
print(re.search('[0-9a-fA-F]','--- a0 ---')) # <re.Match object; span=(4, 5), match='a'>

# you can compliment a character class by specifying ^ as the first character
# in this case it will match any character that is not in the case
print(re.search('[^0-9]', '12345foobar')) # <re.Match object; span=(5, 6), match='f'>

# if ^ is not the first character, then it has no special meaning
print(re.search('[0-9#&^]', 'foo^bar#qux')) # <re.Match object; span=(3, 4), match='^'>

# if you need to search for hyphen, place it as the first or last character or escape it with a backslash (\)
print(re.search('[-abc]', '123-456'))  # <re.Match object; span=(3, 4), match='-'>
print(re.search('[abc-]', '123-456'))  # <re.Match object; span=(3, 4), match='-'>
print(re.search('[ab\-c]', '123-456')) # <re.Match object; span=(3, 4), match='-'>

# if you need to search for ']', place it as the first char escape it with backslash
print(re.search('[]]', 'foo[1]'))       # <re.Match object; span=(5, 6), match=']'>
print(re.search('[ab\]cd]', 'foo[1]'))  # <re.Match object; span=(5, 6), match=']'>

# other special characters lose their special meanings inside a character class
print(re.search('[)*+|]', '123*456')) # <re.Match object; span=(3, 4), match='*'>
print(re.search('[)*+|]', '123+456')) # <re.Match object; span=(3, 4), match='*'>

