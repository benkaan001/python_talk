'''
Twin primes are pairs of primes which differ by two. 
The first twin primes are {3,5}, {5,7}, {11,13} and {17,19}.

'''

num= 31


def isprime(num):
    
    for i in range(2,num):
        if(num  % i == 0):
            return False
    
    return True

# test isprime
# print(isprime(31)) # True




def get_twins():
    
    prime_nums=[i for i in range(2, num) if isprime(i)] # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    output = []
    
    for i in range(len(prime_nums) -1):
        if prime_nums[i+1] - prime_nums[i] == 2:
            output.append( ( str(prime_nums[i]) + ":" + str(prime_nums[i+1]) ) )
            
    return output
"""
output = [] 

i = 0 | i = 1            | i = 2                   | i = 3 | i = 4                            | i = 5 | i = 6                                     | i = 7 | i = 8 
      |                  |                         |       |                                  |       |                                           |       | 
      | output = ['3:5'] | output = ['3:5', '5:7'] |       | output = ['3:5', '5:7', '11:13'] |       | output = ['3:5', '5:7', '11:13', '17:19'] |       | 

"""

output = get_twins() # ['3:5', '5:7', '11:13', '17:19']

final_output = ",".join(i for i in output)

print(final_output) # 3:5,5:7,11:13,17:19
            

# def generate_twins(end):
#     output=""
#     for i in range(2,end):
#         j=i+2
#         if(isprime(i) and isprime(j)):
#             output+=f'{i}<>{j},' #  output = '3<>5,5<>7,11<>13,17<>19,' 
#     return output.strip(',')
#
# print(generate_twins(20)) # 3<>5,5<>7,11<>13,17<>19

