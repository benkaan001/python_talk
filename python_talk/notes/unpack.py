'''
a, b = 1, 2        -> a=1 & b=2
a, b = 1, 2, 3     -> ValueERROR 
a, b, c = 1,2      -> ValueEROOR

'''

# Use _ for variables that will not be used

calories= 100, 200
apple, _ = calories 
print(apple) #100

calories = 100, 200, 300, 400, 500
_, banana, mango, *etc = calories
print(banana) # 200
print(mango) # 300
print(etc) # [400,500]

apple, banana, *etc, durian = calories
print(durian) # 500
print(etc) # [300,400]


#        FUNCTION RETURN VALUE UNPACKING
# Refer to scope/pass_by_assignment

# the function returns multiple values
def greet(name, counter):
    return f"Hi, {name}!", counter+1

# the issue is that since the greet function returns multiple values
# we get a tuple
def main():
    counter = 0
    print(greet("Irma", counter))
    print(f"Counter is {counter}")
    print(greet("Veda", counter))
    print(f"Counter is {counter}")

main()
"""
('Hi, Irma!', 1)
Counter is 0
('Hi, Veda!', 1)
Counter is 0
"""

# to fix this issue, we can reassign the counter variable with each call to greet()
def main2():
    counter = 0
    greeting, counter = greet("Irma", counter)
    print(f"{greeting}\nCounter is {counter}")
    greeting, counter = greet("Veda", counter)
    print(f"{greeting}\nCounter is {counter}")
    
main2()

"""
Hi, Irma!
Counter is 1
Hi, Veda!
Counter is 2


"""