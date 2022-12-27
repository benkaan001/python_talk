# @ syntax does not work if the wrapper function takes in arguments


def decorator_func(callback_func):
    def wrapper_func():
        print(
            f"Wrapper executed this before executing {callback_func.__name__.upper()} function! "
        )
        return callback_func()

    return wrapper_func


@decorator_func
def callback(arg1, arg2):
    print("Executed callback function with args: {arg1} and {arg2}")


try:
    callback("Tom", "Jerry")
except Exception as e:
    print(
        e
    )  # decorator_func.<locals>.wrapper_func() takes 0 positional arguments but 2 were given
