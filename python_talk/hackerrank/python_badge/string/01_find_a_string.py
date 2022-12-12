"""
    Find the number of times that substring occurs in a given string.
    
    INPUT: 
        s = "ABCDCDC"
        sub = "ABC"
    
    EXPECTED OUTPUT -> 2
    
    
"""

s = "ABCDCDC"
sub = "CDC"



def count_substring(s, sub):
    count = 0
    for i,_ in enumerate(s):
        if s[i:].startswith(sub):
            count += 1
    return count
    
    
print(count_substring(s, sub)) # 2


