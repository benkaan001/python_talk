"""
    Recursion breaks a complex problem into a combination of less complex
    problems. 
    
    Recursion logic consists of two parts: BASE CASE and RECURSIVE CASE
    
    BASE CASE -> gives us the ultimate return value of the samaller function
    
    RECURSIVE CASE -> is where the larger problem gets dismanteled into smaller pieces.

"""

# Notice that without a transformation logic, fibo simply returns the value of base case.
# That is why we need to incorporate an accumulation logic into our recursive case.
def fibo(n):
    
    if n < 2: 
        # base case
        return 1
    else:
        # recursive case 
        return fibo(n-1)

print(fibo(100)) # 1


# With an accumulator logic incorporated in our recursive case
def fibo2(n):
    
    if n < 2:
        return 1
    else:
        return n * fibo2(n-1)
    
for i in range(10):
    print(f"i={i}: {fibo2(i)}")
    """
        i=0: 1
        i=1: 1
        i=2: 2
        i=3: 6
        i=4: 24
        i=5: 120
        i=6: 720
        i=7: 5040
        i=8: 40320
        i=9: 362880
    
    """

# MUTUALLY INTERDEPENDENT RECURSION takes place when function x calls function y
# and function y in return calls function x while each having different base cases.

def ping(i):
    
    if i > 0:
        return pong(i-1)
    else:
        return "0"
    
    
def pong(i):
    
    if i > 0:
        return ping(i-1)
    else:
        return "1"
    

# For even numbers, our base case always resolves to 0 regardless of the size of the argument
# For odd numbers, it is vice versa

print(ping(2))  # 0
print(ping(40)) # 0
print(ping(1))  # 1
print(ping(13)) # 1
