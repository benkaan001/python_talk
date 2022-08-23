
lst = ['eat', 'your','vegetables']
lst2 = [*lst, None, None, None]
lst3 = [1.0, 3.3, 'a', False, True, None, (1,2)]

# DELIMITER SETS THE TONE

print(''.join(lst))     # eatyourvegetables
print(' '.join(lst))    # eat your vegetables
print('\t'.join(lst))   # eat    your    vegetables


# ONE-LINERS

print(', '.join('"' + x + '"' for x in lst)) 
# "eat", "your", "vegetables"


print('_'.join(x for x in lst2 if x != None)) 
# eat_your_vegetables


print(','.join(str(x) for x in lst3)) 
# 1.0,3.3,a,False,True,None,(1, 2)





def concat(*args, sep="/"):
    return sep.join(args)

print(concat("A", "B", "C", sep=",")) # A,B,C