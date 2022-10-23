'''
Python has at least two distinguishable kinds of errors:
    syntax errors -> Errors detected during parsing: FATAL
    exceptions -> Errors detected during execution: CAN BE HANDLED
'''

# syntax errors, aka parsing errors,
while True print("Hello")  --> missing colon(:)
"""
File "/Users/benkaan/Desktop/python_talk/python_talk/notes/exceptions/01_exceptions101.py", line 8
    while True print("Hello")
               ^
SyntaxError: invalid syntax
"""
