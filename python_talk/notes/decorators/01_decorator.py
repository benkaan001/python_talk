# A decorator is a function that takes another function OBJECT as an argument
# adds some kind of functionality to it and returns another function OBJECT.


def decorator_func(callback_func):
    def wrapper_func():
        return callback_func()

    return wrapper_func


def callback():
    print("Executed callback function")


decorated_callback = decorator_func(callback)
decorated_callback()  # Executed callback function
