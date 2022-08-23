#formatting string
# methods --> % , .format() , f-Strings

var1 = 'Tom'      # %s for string
var2 = 3          # %d for int
var3 = 3.455343   # %f for float
var4= 'potatoes'

str1 = 'the variable is %s' %var1 # the variable is Tom
str2= 'the integer is %d' %var2   # the integer is 3
str3 =' the floating is %f' %var3 # the floating is 3.455343
str32= 'i want two digits of the float %.2f' %var3  #3.46


# NEW WAY OF FORMATTING

new1 = 'the floating is {}'.format(var3)  #the floating is 3.455343
new2 = 'this is a test float {:.2f}'.format(var3)  #3.46
new3 = 'He eats {} {} times a day!'.format(var4,var2)
# He eats potatos 3 times a day!



# NEWER WAY OF FORMATTING as of py3.6

#evaluates it at run-time so we can manipulate by running operations
newest =f'He eats {var4.upper()} {var2*7} times a week!'
# He eats POTATOES 21 times a week!