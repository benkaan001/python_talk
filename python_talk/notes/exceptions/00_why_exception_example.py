def total_calories(calorie_list):
    
    cal_sum = 0
    
    for calorie in calorie_list:
        if(type(calorie) is int): 
            cal_sum+=calorie
        else:
            print("Wrong input type")
            break
    print(cal_sum)
    
total_calories([100,90,30, "40", 100]) 

# Prints both Wrong input type and 220