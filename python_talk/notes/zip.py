# We can opt out for zip instead of enumurate
 
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC','Marvel', 'DC']

for name,hero,universe in zip(names,heroes,universes):
    print(f"{name} is actually {hero} from {universe}")

'''
    Peter Parker is actually Spiderman from Marvel
    Clark Kent is actually Superman from DC
    Wade Wilson is actually Deadpool from Marvel
    Bruce Wayne is actually Batman from DC
'''