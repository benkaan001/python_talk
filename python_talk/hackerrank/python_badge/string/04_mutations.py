"""

Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string


"""


def mutate_string(s, pos, char):
    
    out = [i for i in s]
    out[pos] = char

    return "".join(i for i in out)
    
s = "abracadabra"
pos = 5
char = 'k'

print(mutate_string(s, pos, char)) # abrackdabra




def mutate_string2(s, pos, char):
    
    return s[:pos]+char+s[pos+1:]

print(mutate_string2(s, pos, char))