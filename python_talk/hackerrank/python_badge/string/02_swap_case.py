"""
    You are given a string and your task is to swap cases. 
    In other words, convert all lowercase letters to uppercase letters and vice versa.
    
    Www.HackerRank.com     →     wWW.hACKERrANK.COM
    Pythonist 2     →     pYTHONIST 2  

"""


def swap_case(s):
    return ''.join([l.lower() if l == l.upper() else l.upper() for l in s])

s1 ="HackerRank.com presents 'Pythonist 2'"

print(swap_case(s1)) # hACKERrANK.COM PRESENTS 'pYTHONIST 2'


def swap_case2(s):
    output = ""
    for char in s:
        if char.islower():
            output += char.upper()
        else:
            output += char.lower()
            
    return output

print(swap_case2(s1)) # hACKERrANK.COM PRESENTS 'pYTHONIST 2'