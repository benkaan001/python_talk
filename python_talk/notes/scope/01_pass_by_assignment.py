"""
Pass by reference -> 
    
    argument that you are passing to a funciton is a reference to a variable
    that already exists in the memory rather than an independent copy of that
    argument

Pass by value ->

    arguments that you pass become independent copies of the original values.
"""

# Python passes arguments neither by reference nor by value, but by assignment.
# Built-in id returns the memory location of the desired object
# Both function arguments refer to the same address as thier original variables
# However, reassigning the argument within the function gives it a new addres
# while the original variable remains unmodified.
# The fact that initial addresses of n and x are the same when you invoke increment()
# proves that the argument x is not passed by value. Otherwise, both x and n would have
# distinct memory addresses 
def main():
    n = 9001
    print(f"Initial address of n: {id(n)}")
    increment(n)
    print(f"  Final address of n: {id(n)}")
    
def increment(x):
    print(f"Initial address of x: {id(x)}")
    x += 1
    print(f"  Final address of x: {id(x)}")

main()

"""
Initial address of n: 4444204912
Initial address of x: 4444204912
  Final address of x: 4445410192
  Final address of n: 4444204912

"""