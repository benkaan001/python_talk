class Inventory:
    available_units = 100
    def out(self):
        self.available_units-=1
        return print(f'Units left: {self.available_units}')
        

shirts = Inventory()
shirts.out() # 99
shirts.out() # 98

pants = Inventory()
pants.out() # 99
pants.out() # 98

print(type(pants)) # <class '__main__.Inventory'>

# dir() returns list of attributes and methods of any object
print(dir(pants))
"""
['__class__', '__delattr__', '__dict__', 
'__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 
'available_units', 'out']
"""

print(dir(Inventory))

"""
['__class__', '__delattr__', '__dict__', 
'__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 

        *** CUSTOM ATTRIBUTES AND METHODS LISTED IN THE END OF THE LIST ***

        'available_units', 'out']
"""



languages = ['Python','JS','Java','Scala','C+']
print(dir(languages))

"""
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 


    *** __DOUBLE UNDERSCORED ITEMS BELONG TO INTERNAL WORKINGS PYTHON__ ***

    'append', 'clear', 'copy', 'count', 'extend', 'index', 
    'insert', 'pop', 'remove', 'reverse', 'sort']

"""
