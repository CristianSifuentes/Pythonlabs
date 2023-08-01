# creating a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75, 10, 20,25.75 )
print(number_tuple) # (10, 20, 25.75)

# string tuple
string_tuple = ('Jessa', 'Emma', 'Kelly')
print(string_tuple) # 
print('0 => ', string_tuple[0]) # 0 =>  Jessa
print('-1 => ', string_tuple[-1]) # -1 =>  Kelly

# mixed type tuple
sample_tuple = ('Jessa', 30, 45.75, [25, 78])
print(sample_tuple)

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Jessa', 30, 45.75, [25, 78]))
print(sample_tuple2)

# without coma
single_tuple = ('Hello')
print(type(single_tuple)) # <class 'str'>
print(single_tuple)  # Hello

# with comma
single_tuple1 = ('Hello',)
print(type(single_tuple1)) # <class 'tuple'>
print(single_tuple1) # ('Hello',)

# Crud
# number_tuple.append(10) # AttributeError: 'tuple' object has no attribute 'append'
# number_tuple[1] = 4
# print(number_tuple) # TypeError: 'tuple' object does not support item assignment

print(number_tuple.index(20)) # 1
print(number_tuple.index(25.75)) # 2
print(number_tuple.count(25.75)) # 2 becaus exists 2 elements '25.75'

my_list = list(number_tuple)
print(my_list) # [10, 20, 25.75, 10, 20, 25.75]
print(type(my_list)) # <class 'list'>

my_list[1] = 56
print(my_list) # [10, 56, 25.75, 10, 20, 25.75]

my_tuple = tuple(my_list)
print(my_tuple) # (10, 56, 25.75, 10, 20, 25.75)