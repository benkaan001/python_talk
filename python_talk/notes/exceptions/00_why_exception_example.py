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

"""
calorie_list = [100, 90, 30, '40', 100] 

cal_sum = 0 

calorie = 100 | calorie = 90  | calorie = 30  | calorie = '40' 
              |               |               | 
cal_sum = 100 | cal_sum = 190 | cal_sum = 220 | 
              |               |               | 
              |               |               | print('Wrong input type') 
              |               |               | 
print('220') 

"""