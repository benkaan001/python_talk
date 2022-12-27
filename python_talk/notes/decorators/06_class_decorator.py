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


callback("Tom", "Jerry")


# converting the function decorator into a class decorator


class decorator_class(object):
    def __init__(self, callback_func):
        self.callback_func = callback_func

    def __call__(self, *args, **kwargs):
        print(
            f"Dunder call method executed this before executing {self.callback_func.__name__.upper()} function! "
        )
        return self.callback_func(*args, **kwargs)


@decorator_class
def callback(arg1, arg2):
    print(f"Executed callback function with args: | {arg1} and {arg2} |")


callback("Tom", "Jerry")
# Dunder call method executed this before executing CALLBACK function!
# Executed callback function with args:| Tom and Jerry |
