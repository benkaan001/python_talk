'''
Twin primes are pairs of primes which differ by two. 
The first twin primes are {3,5}, {5,7}, {11,13} and {17,19}.

'''

num= 31


def is_prime(num):
    
    for i in range(2,num):
        if(num  %i == 0):
            return False
    
    return True

print(is_prime(31)) # true

prime_nums=[]
for i in range(2,num):
    if is_prime(i):
        prime_nums.append(i)

print(prime_nums)

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def generate_twins(end):
    output=""
    for i in range(2,end):
        j=i+2
        if(is_prime(i) and is_prime(j)):
            output+=f'{i}<>{j},'
    return output.strip(',')

print(generate_twins(20))