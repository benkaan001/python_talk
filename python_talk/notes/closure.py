'''
Three conditions:
  1) A nested/inner function must exist
  2) Inner function must refer to a value definied in the outer function
  3) Outer function must RETURN the inner function
'''

def outer (x):
    y= 4
    def inner(z):
        print(f"x={x}, y={y}, z={z}")
        return x+y+z
    return inner

for i in range (3):
    closure = outer(i)
    print(f"closure({i+5}) = {closure(i+5)}")
    
'''
x=0, y=4, z=5
closure(5) = 9
x=1, y=4, z=6
closure(6) = 11
x=2, y=4, z=7
closure(7) = 13
'''
    
    

def print_msg(msg):
    
    def printer():
        print(msg)
    
    printer()

message= print_msg("hello")  #hello



# notice that the inner function is being returned without being invoked

def return_msg(msg):
    
    def printer():
        print(msg)
        
    return printer

# bounding the inner function to message variable
message = return_msg("returning message")


# invoking the inner function 
message()


# after deleting the outer function, the child still has access to its parent's lexical environment 
del return_msg
message() # returning message
return_msg('is there anyone there!?') 
#NameError: name 'return_msg' is not defined

