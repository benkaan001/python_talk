
def halloween_sale(p,d,m,s):
    """ rename args for readability """
    
    game_count = 0
    first_game = p
    discount = d
    budget = s
    min_cost = m 
    
    while budget >= 0:
        budget -= first_game
        first_game = max((first_game - discount), min_cost)
        game_count+=1
        
    """
    budget = 65     | budget = 48     | budget = 34     | budget = 23    | budget = 15    | budget = 9     | budget = 3     | budget = -3 
    first_game = 17 | first_game = 14 | first_game = 11 | first_game = 8 | first_game = 6 | first_game = 6 | first_game = 6 | first_game = 6 
    game_count = 1  | game_count = 2  | game_count = 3  | game_count = 4 | game_count = 5 | game_count = 6 | game_count = 7 | game_count = 8 
    
    """
        
    return game_count -1

#result = halloween_sale(20, 3, 6, 70) #5
result = halloween_sale(20, 3, 6, 85) #7
print(result)

# alternative approach that breaks out of the while loop if budget goes below zero

def halloween_sale_alternative(p,d,m,s):
    game_count = 0
    first_game = p
    discount = d
    budget = s
    min_cost = m 
    
    while budget >= 0:
        budget -= first_game
        first_game = max((first_game - discount), min_cost)
        # alternative conditional check 
        if budget >= 0:
            game_count += 1
        else:
            break
        
    return game_count

alt_result = halloween_sale_alternative(20, 3, 6, 85)
print(alt_result)