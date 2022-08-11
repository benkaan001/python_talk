'''
a, b = 1, 2        -> a=1 & b=2
a, b = 1, 2, 3     -> ValueERROR 
a, b, c = 1,2      -> ValueEROOR

'''

# Use _ for variables that will not be used

calories= 100, 200
apple, _ = calories 
print(apple) #100

calories = 100, 200, 300, 400, 500
_, banana, mango, *etc = calories
print(banana) # 200
print(mango) # 300
print(etc) # [400,500]

apple, banana, *etc, durian = calories
print(durian) # 500
print(etc) # [300,400]



