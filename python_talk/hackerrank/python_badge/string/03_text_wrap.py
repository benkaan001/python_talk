"""
    You are given a string  S and width w .
    Your task is to wrap the string into a paragraph of width w .
    
    SAMPLE INPUT:
    
    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4
    
    SAMPLE OUTPUT:
    
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ
    
"""

def wrap(s, w):
    
    last = len(s) % w 
    last = s[len(s)-2:]
    
    output = []
    
    for i in range(1,len(s[::w])):
        temp = s[(i-1)*w:(i*w)]
        output.append(temp)
    
    if len(last) >0:
        output.append(last)
    
    out = "\n".join(i for i in output)
    return out 
    


s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4

print(wrap(s,w))


output = ['ABCD', 'EFGH', 'IJKL', 'IMNO', 'QRST', 'UVWX', 'YZ'] 

out = 'ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ' 