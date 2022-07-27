# STRING - INTEGER - FLOAT - BOOLEAN - TUPLE - (COMPLEX, FROZEN SETS, BYTES)

# let's assume that we want to convert meow to Meow

sound = "meow"
id(sound)    # 4487467312

try:
    sound[0] = "M"   # TypeError: 'str' object does not support item assignment
    
except TypeError:
    print("Can't touch that!")


# When string reference is reinitialized with a new value, a new object
#gets created instead of overriding the previous value

sound = "Meow"
id(sound)     # 4519967408

# When two identifiers refer to the same immutable object, they share
# the same memory location

lunch_special1="tacos"
id(lunch_special1)  # 4490839472

lunch_special2="tacos" 
id(lunch_special2)  # 4490839472

#___________________________________________________________________________________#

# TUPLE demonstrates both mutablity and immutability 
# depending on the element that we are trying to manipulate 

flexible_tuple =( "potato", [1,2,3,4])
print(id(flexible_tuple)) # 4471473728 

# let's try to convert potato to Potato
try:
    flexible_tuple[0] = flexible_tuple[0].title() # TypeError: 'tuple' object does not support item assignment
except Exception:
    print("Can't touch that!")


flexible_tuple[1].append(5) # ('potato', [1, 2, 3, 4, 5])
print(id(flexible_tuple)) # 4471473728 -> still same memory location


