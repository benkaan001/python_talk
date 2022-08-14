
def migratory_birds(arr):
    
    count = [0]*len(arr)
    for num in arr:
        count[num] += 1
    return count.index(max(count))


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
result = migratory_birds(arr)
print(result) #3


def migratory_birds_destructure_practice(arr):
    
    bird_set = {num:arr.count(num) for num in arr}
    bird_list = [(x,y) for x,y in bird_set.items()]
    sorted_bird_list = sorted(bird_list, key=lambda x:x[1], reverse=True)
    bird_keys = [key for (key,_) in sorted_bird_list]
    bird_values = [value for (key,value) in sorted_bird_list]
    
    if bird_values[0] > bird_values[1]:
        return bird_keys[0]
    elif bird_values[0] == bird_values[1]:
        return bird_keys[0] if bird_keys[0] < bird_keys[1] else bird_keys[1]
    
result2 = migratory_birds_destructure_practice(arr)
print(result2) #3