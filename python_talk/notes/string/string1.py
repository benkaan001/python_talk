
#Strings are ordered and immutalbe 

my_string = "hello pyton"

substring= my_string[1:5] #'ello'
no_beginning = my_string[:5] #'hello'
reverse = my_string[::-1] # 'notyp olleh'

name="Tom"
sentence = name + " says " + no_beginning

# loop through a string

for i in my_string:
    print(str(i).upper())
    
# check if a letter is in a string

if 'e' in my_string:
    print("yes")
else:
    print("no")
    

str1= "  I have white space    "
copy1 =str1.strip()
print(copy1) # 'I have white space'

str2 = "Too much money"
print(str2.startswith("t"))
print(str2.startswith("Too"))
print(str2.endswith("ney"))

#find index

str3="Where have you benn?"
print(str3.find('e')) #only the first instance of 2, which is at 2
print(str3.index("e")) # again prints 2
print(str3.find('z')) # will return -1 if it does not find

str4 ="yet another amazing day at the office"
print(str4.count('a')) # 5 
print(str4.title()) # Yet Another Amazing Day At The Office



str5 = "replacable replacable employees"
print(str5.replace('replacable', 'irreplacable', 1))
#irreplacable replacable employees 
