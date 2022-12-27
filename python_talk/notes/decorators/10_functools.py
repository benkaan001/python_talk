import time
import logging
from functools import wraps

# in order to preserve the original functionality of the callback_func
# we need to decorate each of the wrapper function with functools' wraps() method.


def my_logger(callback_func):
    """Creates a log file at the location specified in the filename that logs
    the arguments passed into callback function"""

    logging.basicConfig(
        filename=f"/Users/benkaan/Desktop/python_talk/python_talk/notes/decorators/{callback_func.__name__}.log",
        level=logging.INFO,
    )

    @wraps(callback_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executed with args: {args}, {kwargs}")
        return callback_func(*args, **kwargs)

    return wrapper


def my_timer(callback_func):
    import time

    """Measures the time it takes to execute the callback function passed"""

    @wraps(callback_func)
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
    print(f"Executed callback function with args: | {arg1} and {arg2}|")


callback("TOM1", "JERRY1")
