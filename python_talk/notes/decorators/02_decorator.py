# decorating functions allow us to easily add functionality insdie the wrapper function
# without modifying the original call back function


def decorator_func(callback_func):
    def wrapper_func():
        print(
            f"Wrapper executed this before executing {callback_func.__name__.upper()} function! "
        )
        return callback_func()

    return wrapper_func


def callback():
    print("Executed callback function")


decorated_callback = decorator_func(callback)
decorated_callback()

# Wrapper executed this before executing CALLBACK function!
# Executed callback function
