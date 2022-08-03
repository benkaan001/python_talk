from itertools import groupby

a = [1,2,3,4]

def smaller_than_three(x):
    return "small" if x < 3 else "big"

# returns an iterable object
group_obj = groupby(a, key=smaller_than_three)
# '<itertools.groupby object at 0x10dfeed10>'

for key,value in group_obj:
    print(key, value)
    # small <itertools._grouper object at 0x10b0d93d0>
    # big <itertools._grouper object at 0x10b02c760>


# notice that we still need to unpack the value object
for key,value in group_obj:
    print(key, list(value))
    # small [1, 2]
    # big [3, 4]
    

""" refactor it to make it more `pythonic` """

group_obj = groupby(a, lambda x : "small" if x<3 else "big")

output = [(key,list(value)) for key,value in group_obj]
# [(small, [1, 2]), (big, [3, 4])] 



# BETTER EXAMPLE

students = [{'name': 'Tim', 'GPA': 4.0}, {'name': 'Clare', 'GPA': 4.0},
            {'name': 'Bonnie', 'GPA': 4.0}, {'name': 'Sam', 'GPA': 3.9},
            {'name': 'Pam', 'GPA': 3.8}, {'name': 'Jack', 'GPA': 3.8}]

groupby_obj = groupby(students, key=lambda x: x['GPA'])

for key,value in groupby_obj:
    print("--", key, "--")
    for dicty in value:
        print(dicty['name'])

"""
-- 4.0 --
Tim
Clare
Bonnie
-- 3.9 --
Sam
-- 3.8 --
Pam
Jack

"""
