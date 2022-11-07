
sample_dict = {"Apple": 1300, "Samsung": 900, "LG": 600, "Others": 400}

# logical error
def get_price(brand):
    
    for key,value in sample_dict.items():
        if (key == brand):
            return value 
        else:
            return "Brand not found"

print(get_price("LG")) # Brand not found 



def get_price_right(brand):
    
    if brand in sample_dict.keys():
        return sample_dict[brand]
    else:
        return "Brand not found"
        
print(get_price_right("LG")) # 600
        