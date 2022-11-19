'''
    Anchors don't match any actual characters in the search string.
    Instead, they dictate where a special match should occur.
    
    ^ or \A
    $ or \Z 
    
    For instance, ^foo states foo should be  at the beginning whereas
    baz$ dictatces baz should be at the end of the search string.
    
'''

import re 

print(re.search('^foo', 'foobar')) # <re.Match object; span=(0, 3), match='foo'>
print(re.search('\Afoo', 'foobar')) # <re.Match object; span=(0, 3), match='foo'>
print(re.search('^foo', 'barfoo')) # None
print(re.search('\Afoo', 'barfoo')) # None


print(re.search('bar$', 'foobar')) # <re.Match object; span=(3, 6), match='bar'>
print(re.search('bar\Z', 'foobar')) # <re.Match object; span=(3, 6), match='bar'>
print(re.search('bar$', 'barfoo')) # None

"""
    /b
    
    word boundary anchor dictates the word exists as a word independently of other
    words in the string.

"""

print(re.search(r'\bbar', 'foo bar')) # <re.Match object; span=(4, 7), match='bar'>
print(re.search(r'\bbar', 'foo.bar')) # <re.Match object; span=(4, 7), match='bar'>
print(re.search(r'\bbar', 'foobar')) # None

print(re.search(r'foo\b', 'foo bar')) # <re.Match object; span=(0, 3), match='foo'>
print(re.search(r'foo\b', 'foo.bar')) # <re.Match object; span=(0, 3), match='foo'>
print(re.search(r'foo\b', 'foobar')) # None
