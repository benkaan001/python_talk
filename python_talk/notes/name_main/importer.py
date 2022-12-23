import namemain_func_script, func_script

# notice both functions inside func_script module get invoked when not wrapped
# in namemain - aka unwanted side effect
# regardless of later invocations referencing func_script throughout the module
print("helloooo")
namemain_func_script.func_wrapped_in_namemain()
func_script.unwrapped_func2()

"""
Inside unwrapped function 1.
Inside unwrapped function 2.
helloooo
Inside function wrapped in namemain.
Inside unwrapped function 2.
"""
