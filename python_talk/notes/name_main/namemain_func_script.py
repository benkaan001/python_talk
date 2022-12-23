def func_wrapped_in_namemain():
    print("Inside function wrapped in namemain.")


if __name__ == "__main__":
    func_wrapped_in_namemain()


"""
if we do NOT wrap some_func() function call inside  the if__name == "__main__" block,
the function will be invoked when the func_script module is imported
by another script.
"""
