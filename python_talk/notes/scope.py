'''
    immutable      ->    pass by value
    mutable        ->    pass by reference

'''
a = 1
b = [10]

def func(a,b):
    a+=1
    b+=[1]
    return print(a,b, sep=", ") 

func(a, b) # 2, [10,1]

print(a) # 1
print(b) # [10, 1]

print(a in b) # True 
