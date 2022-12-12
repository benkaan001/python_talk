"""
    You are asked to ensure that the first and last names of people 
    begin with a capital letter in their passports. 
    For example, alison heck should be capitalised correctly as Alison Heck.
    
    Note: in a word only the first character is capitalized. 
    Example 12abc when capitalized remains 12abc.
    
"""

def solve(s):
    
    out = []
    
    for name in s.split():
        out.append(name.capitalize())
        
    return " ".join(name for name in out)

s = "alison heck"
print(solve(s)) #Alison Heck


# Due to this constraint, title() is failing test cases
s2 = "john 123smith"
print(solve(s2)) # John 123smith