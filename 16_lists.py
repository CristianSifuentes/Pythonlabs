
# Using list constructor
my_list1 = list((1, 2, 3))
print("list using constructor => ", my_list1) # Output [1, 2, 3]

# create list using square brackets []
my_list2 = [1, 2, 3]
print("list using square brackets => ", my_list2) # Output [1, 2, 3]



# create list with heterogeneous items
my_list = ['Jessica', 10, 10, 'Kelly', 50, 10.5]
# print entire list
print("list using heterogeneous items => ",my_list) # ['Jessica', 10, 10, 'Kelly', 50, 10.5]

print(type(my_list)) # <class 'list'>

# empty list using list()
my_list4 = list()
print("using empty list () => ", my_list4)

# empty list using []
my_list5 = []
print("list using empty [] => ", my_list5)


# -----------------------------------------------

print(len(my_list))

# Accessing 1st element of a list
print(my_list[0]) # Jessica

# Accessing last element of a list
print(my_list[-1]) # 10.5

# access chunks of list data
print(my_list[1:3]) # [10, 10]

# Modifying first element of a list
my_list[0] = 'Emma'
print(my_list[0]) # Emma

# add one more elements to list
my_list.append(100)
print(my_list) # ['Emma', 10, 10, 'Kelly', 50, 10.5, 100]

print(type(my_list).__name__) # list
