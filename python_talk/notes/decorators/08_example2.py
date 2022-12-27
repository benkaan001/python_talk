import time


def my_timer(callback_func):

    """Measures the time it takes to execute the callback function passed"""
    # import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = callback_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{callback_func.__name__} ran in {t2} second(s)")
        return result

    return wrapper


@my_timer
def callback(arg1, arg2):
    time.sleep(1)  # pause for 1 second before the callback is executed
    print(f"Executed callback function with args: | {arg1} and {arg2} |")


callback("Tom", "Jerry")
# Executed callback function with args:| Tom and Jerry |
# callback ran in 1.0050668716430664 second(s)
