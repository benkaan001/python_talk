def unwrapped_func1():
    print("Inside unwrapped function 1.")


def unwrapped_func2():
    print("Inside unwrapped function 2.")


unwrapped_func1()
unwrapped_func2()


"""
When this module is imported by another script, both functions will automatically
be invoked
"""
