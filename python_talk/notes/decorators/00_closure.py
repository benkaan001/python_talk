def outer_func():
    message = "Outer message"

    def inner():
        print(f"Printing the message from outer: {message}")

    return inner()


outer_func()  # Printing the message from outer: Outer message
call_outer = outer_func()
call_outer  # Printing the message from outer: Outer message


# Even after executing the outer function, the program keeps the inner function
# in memory and enables us to assign it to a variable and call it when needed.


def outer():
    message = "Outer message"

    def inner():
        print(f"Printing the message from outer: {message}")

    return inner


callable_var = outer()
callable_var()  # Printing the message from outer: Outer message


# Example with arguments
def outer2(msg):
    def inner():
        print(f"Printing the message from outer {msg}")

    return inner


callable_var1 = outer2("First message")
callable_var2 = outer2("Second message")
callable_var1()  # Printing the message from outer First message
callable_var2()  # Printing the message from outer Second message
