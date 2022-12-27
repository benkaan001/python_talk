import time
import logging

# in order to run multiple decorators we need to stack them
# stacking order determines the execution order


def my_logger(callback_func):
    """Creates a log file at the location specified in the filename that logs
    the arguments passed into callback function"""

    logging.basicConfig(
        filename=f"/Users/benkaan/Desktop/python_talk/python_talk/notes/decorators/{callback_func.__name__}.log",
        level=logging.INFO,
    )

    def wrapper(*args, **kwargs):
        logging.info(f"Executed with args: {args}, {kwargs}")
        return callback_func(*args, **kwargs)

    return wrapper


def my_timer(callback_func):

    """Measures the time it takes to execute the callback function passed"""

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = callback_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{callback_func.__name__} ran in {t2} second(s)")
        return result

    return wrapper


@my_logger
@my_timer
def callback(arg1, arg2):
    time.sleep(1)  # pause for 1 second before the callback is executed
    print(f"Executed callback function with args: | {arg1} and {arg2} |")


callback("Tom", "Jerry")

"""
    The code is no longer producing the expected results.

    WHY?

        @my_logger
        @my_timer
        def callback(arg1,arg2):
            ...

    This function call is similar to

    callback = my_logger(my_timer(callback))
    callback("Tom", "Jerry")

    As we can see we are no longer passing the original callback function to the
    outermost function. Instead we are passing the function object, aka wrapper, that
    was returned from my_timer(callback) function. Additionally, notice that my_logger
    creates a wrapper.log file accordingly.

    When we switch the order of decorators, we would be passing my_logger(callback) to the
    my_timer function and would get the inccorrect result.

    SOLUTION -> wraps() from functools module

"""
