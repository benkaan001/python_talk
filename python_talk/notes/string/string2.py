from timeit import default_timer as timer

str1 = "how you doing buddy"

mylist =str1.split() # the default delimiter argument is (" ")

# ['how', 'you', 'doing', 'buddy']


str2 ="this,needs,fixing"
mylist2 = str2.split() # will print ['this,needs,fixing'] as one element
mylist2=str2.split(",") 


#convert from list to string1

list3= ['Happy', 'New', 'Year', 'Wooo Hooo!!!!']
str3= ' '.join(list3) # make sure to leave space in between
# 'Happy New Year Whoo Hoo!!!'

'''
LOOPING THROUGH A STRING IS A VERY EXPENSIVE OPERATION
SINCE A COPY OF A NEW STRING HAS TO BE CREATED 

importing timer to measure the performance
'''
str4 = ['a']*10

start=timer()
bad_practice=''
for i in str4:
    bad_practice+= i

stop=timer()
print(stop -start)

start2=timer()
better_practice = ''.join(str4)
stop2=timer()
print(stop2-start2)