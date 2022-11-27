'''
    General Exception class overrides any of the preceeding exception blocks.
    
    Nevertheless, excluding the Exception class inside the except block 
    before any other specific except block will result in a syntax error.
'''
def calculate_calories(calorie_list):
    
    cal_sum = 0
    
    try:
        for calorie in calorie_list:
            cal_sum += calorie 
        
        return cal_sum
    
    except Exception as e: # e = TypeError("unsupported operand type(s) for +=: 'int' and 'str'")
        print(f"Handled in Exception Block: {e}")
    except TypeError as e: # will not get triggered
        print(f"Handled in TypeError Block: {e}")
    
calculate_calories([100,90,30, "40", 100]) 

# Handled in Exception Block: unsupported operand type(s) for +=: 'int' and 'str'



#####################################################################################

def calculate_calories2(calorie_list):
    
    cal_sum = 0
    
    try:
        for calorie in calorie_list:
            cal_sum += calorie 
    
        return cal_sum

    except:
        print("Plain except block.") 
    except TypeError as e:
        print(f"Handled in TypeError Block: {e}")
    
calculate_calories2([100,90,30, "40", 100]) 

# SyntaxError: default 'except:' must be last