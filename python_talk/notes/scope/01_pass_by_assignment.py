"""
Pass by reference -> 
    
    argument that you are passing to a funciton is a reference to a variable
    that already exists in the memory rather than an independent copy of that
    argument

Pass by value ->

    arguments that you pass become independent copies of the original values.
"""

# Python passes arguments neither by reference nor by value, but by assignment.
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
Initial address of n: 140562586057840
Initial address of x: 140562586057840
  Final address of x: 140562586057968
  Final address of n: 140562586057840

"""