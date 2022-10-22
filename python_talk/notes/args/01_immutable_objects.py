# In python all arguments are passed by REFERENCE
# At the time of function invokation both formal and actual arguments point to the same object


def double_number(formal_num):
    
    print(f"Formal argument value before function call: {formal_num}") # 100
    formal_num *= 2
    print(f"Formal argument value after update inside function: {formal_num}") # 200
    
actual_num = 100
print(f"Actual argument value before function call: {actual_num}")

double_number(actual_num)
print(f"Actual argument value after function call: {actual_num}")

"""
Actual argument value before function call: 100
Formal argument value before function call: 100
Formal argument value after update inside function: 200
Actual argument value after function call: 100


"""