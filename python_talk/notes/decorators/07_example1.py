def my_logger(callback_func):
    """Creates a log file at the location specified in the filename that logs
    the arguments passed into callback function"""

    import logging

    logging.basicConfig(
        filename=f"/Users/benkaan/Desktop/python_talk/python_talk/notes/decorators/{callback_func.__name__}.log",
        level=logging.INFO,
    )

    def wrapper(*args, **kwargs):
        logging.info(f"Executed with args: {args}, {kwargs}")
        return callback_func(*args, **kwargs)

    return wrapper


@my_logger
def callback(arg1, arg2):
    print(f"Executed callback function with args: | {arg1} and {arg2} |")


callback("Tom", "Jerry")
callback("Hansel", "Gretel")
