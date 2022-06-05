'''
Given two input strings, return the common characters.

If no common character found, return 'Not found'

Constraints :
- perform case-sensitive comparison
- ignore non-alphanumeric characters
- do not repeat if there is more than one same type of character
- do not use Set
- disgregard time complexity

'''

s1 = "Life is beautiful"
s2 = "Health is new wealth"

# worst solution imaginable :-P
def find_common(str1, str2):
    list1 = str1.split(' ')
    list2 = str2.split(' ')
    common_list=[]
    for i in range (len(list1)):
        for j in range (len(list2)):
            for letter1 in list1[i]:
                for letter2 in list2[j]:
                    if(letter1 == letter2 and letter1 not in common_list):
                        common_list.append(letter1)
    
    common_chars=''
    
    if (len(common_list) == 0):
        common_chars = 'Not found'
    
    for letter in common_list:
        common_chars+=letter
        
    return print(common_chars)      

find_common(s1,s2) 

find_common('bronze','silk')



''' better alternative Using set '''

set1 = set(s1)  #
set2 = set(s2)
common= set1 & set2
common_list = list(common)
common_chars = ''
for letter in common_list:
    if letter == ' ':
        continue
    common_chars+=letter
print(common_chars)

# condensed expression
short_n_sweet = list(set(s1)&set(s2)) 
# ['e', 'a', 's', 't', 'i', 'l', ' '] 

