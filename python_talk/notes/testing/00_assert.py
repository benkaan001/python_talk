# If the test, or assertion, fails, execution stops
# and an error message gets printed

hair_color = "brown"  # Given hair color is of string type
hair_color = 33  # If hair color is not a string, this will print.

try:
    assert type(hair_color) == str, "If hair color is not a string, this will print."
except Exception as e:
    print(e)
else:
    print("Given hair color is of string type")


# failed assert statements raise an AssertionError exception
assert (
    type(hair_color) == str
), f"Expected hair_color to be a string, but found {type(hair_color)} instead!"

"""

Traceback (most recent call last):
  File "/Users/benkaan/Desktop/python_talk/python_talk/notes/assert.py", line 14, in <module>
    assert (
AssertionError: Expected hair_color to be a string, but found <class 'int'> instead!

"""
