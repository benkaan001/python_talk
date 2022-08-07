class Person():
    pass

person = Person()

# the goal is to set attributes so that the person will look like this:
# person_info = {'first': 'Ben', 'last': 'Kaan'}

first_key = 'first'
first_val = 'Ben'

last_key = 'last'
last_val = 'Kaan'


# setattr(obj, name, value)
setattr(person, first_key, first_val)
setattr(person, last_key, last_val)

print(f"{person.first} {person.last}") # Ben Kaan

print(getattr(person, first_key)) # Ben
print(getattr(person, last_key)) # Kaan

# ______________________ UNPACK _______________________

person2 = Person()

person_info = {'first': 'Veda', 'last': 'Inan'}

for key,value in person_info.items():
    setattr(person2, key, value)

print(f"{person2.first} {person2.last}") # Veda Inan

for key in person_info.keys():
    print(getattr(person2, key))
    # Veda
    # Inan
    


