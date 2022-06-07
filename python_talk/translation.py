'''
Given a color list and a dictionary of color:meaning pairs, 
return the matching meaning of the colors  
'''

def translate(dictionary, colors):
    meanings=[]
    for i in range(len(colors)):
        for key,value in dictionary.items():
            if(colors[i] == key):
                meanings.insert(i,value)
                # meanings.append(value)

    return meanings


dictionary={'Blue': 'Industrious', 'Red': 'Dominant', 'Yellow': 'Optimistic', 'Green': 'Nature', 'Orange': 'Freedom', 'Purple': 'Imagination'}

colors=['Purple', 'Orange', 'Red', 'Blue']

print("The dictionary values were given as:",dictionary)
print('______________________________________________________________________________')

print("Given colors were listed as:",colors)
print('______________________________________________________________________________')
meanings=translate(dictionary, colors)
print("Matching meanings are:",meanings)
print('_______________________________________________________________________________')

