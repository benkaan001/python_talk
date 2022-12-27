# In order to resolve the error, we need to allow our wrapper function to accept
# any number of arbitrary positional or keyword arguments.


def decorator_func(callback_func):
    def wrapper_func(*args, **kwargs):
        print(
            f"Wrapper executed this before executing {callback_func.__name__.upper()} function! "
        )
        return callback_func(*args, **kwargs)

    return wrapper_func


@decorator_func
def callback(arg1, arg2):
    print(f"Executed callback function with args: {arg1} and {arg2}")


try:
    callback("Tom", "Jerry")
except Exception as e:
    print(e)
else:
    print("No exception encountered!")

# Wrapper executed this before executing CALLBACK function!
# Executed callback function with args: Tom and Jerry
# No exception encountered!
