"""
    Given string s 
    Print out in the given order if s contains:
        1) alphanumeric characters
        2) alphabetical characters
        3) digits
        4) lowercase characters
        4) uppercase characters
 
 """
 
s = "qA2"
 
print(any(char for char in s if char.isalnum()))
print(any(char for char in s if char.isalpha()))
print(any(char for char in s if char.isdigit()))
print(any(char for char in s if char.islower()))
print(any(char for char in s if char.isupper()))

# USING eval()

eval_list= ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']
for i in eval_list:
        print(any([eval(f"char.{i}") for char in s]))