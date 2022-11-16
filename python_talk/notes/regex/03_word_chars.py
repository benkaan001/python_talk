'''
    \w matches any alphanumeric word character 
    alphanumeric characters also include underscore(_)
    
    \w -----> [a-zA-Z0-9_] 
    
    \W is the opposite of \w matching anything outside
    alphanumeric characters
    
    \W ----> [^a-zA-Z0-9_]
    
'''

import re 

# ntoice 'a' is the first word character in the string
print(re.search('\w', '#(.a$@%&56'))            # <re.Match object; span=(3, 4), match='a'>
print(re.search('[a-zA-Z0-9_]', '#(.a$@%&56'))  # <re.Match object; span=(3, 4), match='a'>


print(re.search('\W', '_100%&.////'))           # <re.Match object; span=(4, 5), match='%'>
print(re.search('[^a-zA-Z0-9_]', '_100%&.////'))# <re.Match object; span=(4, 5), match='%'>

