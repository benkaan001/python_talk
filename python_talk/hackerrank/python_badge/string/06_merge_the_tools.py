
"""
    Split the given string s by number k into substrings
    Print each substring wihtout repeating characters.
    
    Constraint:
        Remove the second repeating character
        i.e substrings -> 'AAB', 'CAA', 'ADA'
             output    -> 'AB', 'CA', 'AD'
"""

def merge_the_tools(s,k):
    """ Violates the contraint mentioned above """


    # l = [i for i in s]
    l = []
    while len(s) > 0:
        sub = s[0:k]
        l.append(sub)
        s = s[k:]

    print(l) # ['AAB', 'CAA', 'ADA']



    l = [tuple(set(i)) for i in l]
    print(l) # [('A', 'B'), ('A', 'C'), ('A', 'D')]

    out =[]

    for item in l:
        out_str = ""
        for x in item:
            out_str+=x 
        if len(out_str) >0:
            out.append(out_str)

    return out   # ['AB', 'AC', 'AD']

s = 'AABCAAADA'
k = 3

print(merge_the_tools(s, k))


def merge_the_tools2(s,k):
    """ Passes all 21 test cases"""
    
    l = []
    
    while len(s) > 0:
        sub = s[0:k]
        l.append(sub)
        s = s[k:]

    print(l) # ['AAB', 'CAA', 'ADA']
    
    for s in l:
        sub_str = ""
        for char in s:
            if char not in sub_str:
                sub_str += char      
        

s = 'AABCAAADA'
k = 3
merge_the_tools2(s, k)