'''
Syntactic sugar constructs that help build altered and filtered lists, dictionaries, or sets 
from a given list, dictionary, or set. 

Traditional FOR LOOP 


for ( iterable ):

     if ( condition ):
         
         output_expression()


[ output_expression() FOR (iterable) IF (condition) ]
     

'''
import math

# Performing aritmetic operations
sample_list=[1,2,3,4,5]

squared_list =[num**2 for num in sample_list] #[1,4,9,16,25]

squared_dict ={num:num**2 for num in sample_list} # {1:1,2:4,3:9,4:16,5:25}

# Conditional mapping

conditional_list =[num**2 for num in sample_list if num % 2 !=0] # [1,9,25]
conditional_dict ={num:num**2 for num in sample_list if num %2== 0} # {2:4, 4:16}

# Applying function

funky_list =[math.factorial(num) for num in sample_list if type(num) == int] #[1, 2, 6, 24, 120] 

veggies = { ' potato ', ' potato ', ' zucchini ', ' pepper ', ' tomato ', ' pepper '}
veggies2 = {veggie.strip() for veggie in set(veggies)} # {'pepper', 'tomato', 'potato', 'zucchini'} 

# Combining two lists

list1 =[1,2,3]
list2 =[10,20,30]

parallel_list =[(a+b) for a,b in zip(list1,list2)] #[11,22,33]

nested_list = [(a,b) for a in list1 for b in list2 if a != b]
#[(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]


# Flatten a 2-D list

nested_list = [[1,2,3],[10,20,30],[100,200,300]]

flattened_list = [ x for temp_list in nested_list for x in temp_list]
#[1, 2, 3, 10, 20, 30, 100, 200, 300]