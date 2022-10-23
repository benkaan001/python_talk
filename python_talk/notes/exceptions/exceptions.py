"""
     When Python encounters an error while runnig the program, it stops execution and raises an exception.
     Exception is an object with
         Description: What went wrong
         Traceback: Where the problem occured
         
     try:
         # Runs first

     except:
         # Runs if exception occurs in the try block

     else:
         # Runs if the try block * SUCCEEDS *

     finally:
         # This code * ALWAYS * executes


"""

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message, value):
        self.message = message
        self.value  = value


def test_value(num):
    if num > 100:
        raise ValueTooHighError('value is too high!')
    if num < 5:
        raise ValueTooSmallError('value is too small', num)

# test_value(200)

"""
 Traceback (most recent call last):
   File "/Users/benkaan/Desktop/piepy/src/exceptions.py", line 8, in <module>
     test_value(200)
   File "/Users/benkaan/Desktop/piepy/src/exceptions.py", line 6, in test_value
     raise ValueTooHighError('value is too high!')
 __main__.ValueTooHighError: value is too high!

"""
 
try:
    test_value(2) # comment out to see the ValueTooHighError result
    test_value(200)
except ValueTooHighError as err:
    print(err) # value is too high!
except ValueTooSmallError as err:
    print(err.message,"-->", err.value) # value is too small --> 2
else:
    print("No exception has been raised") # will print only if no exception is found in the try 
finally:
    print("Here to stay forever!!!") # will ALWAYS print



"""
    Objective: 
    
    - Write a function that reads a text file and returns data
    
    - Measure time required
    
"""

import logging
import time

# Create logger
logging.basicConfig(filename = "/Users/benkaan/Desktop/problems.Log", 
                    level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required"""
    start_time = time.time()
    try:
        f = open(path)
        data = f.read()
        return data
    # assign the Exception object to err
    except FileNotFoundError as err:
        # log the error if the file does not exist
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"Time required for {path} = {dt}")

data = read_file_timed("/Users/benkaan/Desktop/Hadoopy/CreditCardApplicationData.csv") 
# INFO:root:Time required for /Users/benkaan//Desktop/Hadoopy/CreditCardApplicationData.csv = 0.002004861831665039

data = read_file_timed("/Users/benkaan//Desktop/my_imaginary_file.txt")
# ERROR:root:[Errno 2] No such file or directory: '/Users/benkaan//Desktop/my_imaginary_file.txt'
# INFO:root:Time required for /Users/benkaan//Desktop/my_imaginary_file.txt = 6.389617919921875e-05
"""
Traceback (most recent call last):
  File "/Users/benkaan/Desktop/python_talk/python_talk/notes/exceptions.py", line 90, in <module>
    data = read_file_timed("/Users/benkaan//Desktop/my_imaginary_file.txt")
  File "/Users/benkaan/Desktop/python_talk/python_talk/notes/exceptions.py", line 74, in read_file_timed
    f = open(path, mode="rb")
FileNotFoundError: [Errno 2] No such file or directory: '/Users/benkaan//Desktop/my_imaginary_file.txt'
"""
