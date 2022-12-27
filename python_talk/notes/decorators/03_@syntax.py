def decorator_func(callback_func):
    def wrapper_func():
        print(
            f"Wrapper executed this before executing {callback_func.__name__.upper()} function! "
        )
        return callback_func()

    return wrapper_func


def callback():
    print("Executed callback function")


# adding @decorator_func above callback() function statement is the same as
# assigning decorator_func(callback) to a variable named callback
callback = decorator_func(callback)
callback()
# Wrapper executed this before executing CALLBACK function!
# Executed callback function


def decorator_func(callback_func):
    def wrapper_func():
        print(
            f"Wrapper executed this before executing {callback_func.__name__.upper()} function! "
        )
        return callback_func()

    return wrapper_func


@decorator_func
def callback():
    print("Executed callback function")


callback()
# Wrapper executed this before executing CALLBACK function!
# Executed callback function
