from asyncio.tasks import shield

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
except ValueTooHighError as e:
    print(e) # value is too high!
except ValueTooSmallError as e:
    print(e.message,"-->", e.value) # value is too small --> 2
else:
    print("No exception has been raised") # will print only if no exception is found in the try 
finally:
    print("Here to stay forever!!!") # will ALWAYS print