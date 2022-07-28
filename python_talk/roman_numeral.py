conversion = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def convert_from_roman_to_decimal(roman_string):
    total =0;
    for i in range(len(roman_string) -1):
        left_letter=roman_string[i]
        right_letter=roman_string[i+1]
        if(conversion[left_letter] < conversion[right_letter]):
            total-=conversion[left_letter]
        else:
            total+=conversion[left_letter]
    
    total+=conversion[roman_string[-1]]
    
    return total
        

convert_from_roman_to_decimal('MDI') #1500
# convert_from_roman_to_decimal('CLXV') #165