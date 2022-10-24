'''
If an error is not caught inside a function, it can be caught outside the function
'''
def calculate_average(num1,num2):
    try:
        avg = num1/num2
        print(avg)
    except ZeroDivisionError as e:
        print("Cought inside: Cannot divide by 0", e)
    except ValueError as e:
        print("Cought inside: Wrong value", e)
    except Exception as e: # generic must be the last in the list else runtime error
        print("Cought inside: Generic exception", e)

# CASE #1 -> no error
try:
    calculate_average(100, 300) 
except:
    print("Cought outside!")
# # 0.3333333333333333 


# CASE #2 -> non-specified TypeError that got caught by generic except block 
try:
    calculate_average('A', 300) 
except:
    print("Cought outside!")
# Cought inside: Generic exception unsupported operand type(s) for /: 'str' and 'int'


# CASE #3 -> cannot call the function due to excess argument
try:
    calculate_average(300, 100, 100) 
except Exception as e:
    print("Cought outside!", e)
# Cought outside! calculate_average() takes 2 positional arguments but 3 were given
