
def swap():
    
    global b,a
    # the function is modifying the values of global variables a and b
    # therefore without the global declaration above, we get the UnboundLocalError
    b, a = a, b # UnboundLocalError: local variable 'a' referenced before assignment
    
a,b =1,2

swap() # invocation is raising the Error 
print(a-b) # 1


"""             
    ANOTHER ONE         
    
    """

x = 10

def mess_with_x1():
    
    x = 20
    return x

result = mess_with_x1() # 20


def mess_with_x2():
    
    return x;

result = mess_with_x2() # 10

def mess_with_x3():
    
    """
        Everything is fine until we try to manipulate the value of x
        We need to declare that x is a global variable inside the function,
        in order to avoid this error
    """
    global x
    x+=100 # UnboundLocalError: local variable 'x' referenced before assignment
    return x;

result = mess_with_x3() # 110

"""
    WORK AROUND GLOBAL 
    
"""

z = 10

def get_globalz():
    
    globalz = z
    globalz+=100
    return globalz

result = get_globalz() # 110 


