'''
No matter what is stored in a variable (object), 
a variable can be any type like int, float, str, list, tuple, dict, etc. 
There is a built-in function called type() to get the data type of any variable.
'''

a = 100
print(type(a))  # class 'int'

b = 100.568
print(type(b))  # class 'float'

str1 = "PYnative"
print(type(str1))  # class 'str'

my_list = [10, 20, 20.5, 100]
print(type(my_list)) # class 'list'

my_set = { 'Emma', 'Jessa', 'Kelly' }
print(type(my_set)) # class 'set'

my_tuple = (5, 10, 15, 20, 25)
print(type(my_tuple)) # class 'tuple'

my_dict = { 1: 'William', 2: 'John' }
print(type(my_dict)) # class 'dict'