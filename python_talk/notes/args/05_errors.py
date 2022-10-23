

def print_programmer_profile(name, language = "Python", editor="VSCode", experience="proficient"):
    
    print(f"Name: {name}, language: {language}, editor: {editor}, experience: {experience}")

    
print_programmer_profile("John") # 1 positional
# Name: John, language: Python, editor: VSCode, experience: proficient

print_programmer_profile(name="John") # 1 keyword 
# Name: John, language: Python, editor: VSCode, experience: proficient

print_programmer_profile(name="John", language="Java") # 2 keyword 
# Name: John, language: Java, editor: VSCode, experience: proficient

print_programmer_profile(experience="expert",name="John") # 2 keyword 
# Name: John, language: Python, editor: VSCode, experience: expert

print_programmer_profile("John", "JavaScript", "Eclipse") # 3 positional 
# Name: John, language: JavaScript, editor: Eclipse, experience: proficient

print_programmer_profile("John", language="Scala") # 1 positional 1 keyword 
# Name: John, language: Scala, editor: VSCode, experience: proficient


# Missing required positional argument
try:
    print_programmer_profile()
except Exception as e:
    print(e) # print_programmer_profile() missing 1 required positional argument: 'name'



# duplicate value for the same argument
try:
    print_programmer_profile("John", name="Sandy")
except Exception as e:
    print(e) # print_programmer_profile() got multiple values for argument 'name'
    
# unknown keyword argument
try:
    print_programmer_profile("John", height="6 feet 3 inches")
except Exception as e:
    print(e) # print_programmer_profile() got an unexpected keyword argument 'height'
    
    
    
# non-keyword argument after a keyword argument 
# This results in a Syntax Error, which stops the program 
# For more info, refer to the exceptions directory
try:
    print_programmer_profile(name='John', "SQL")
except Exception as e:
    print(e) # SyntaxError: positional argument follows keyword argument
