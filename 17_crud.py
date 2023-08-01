my_list = list([5,8,'Tom', 7.50])

# Using append()
my_list.append('Emma')
print(my_list) # Output  [5, 8, 'Tom', 7.5, 'Emma']


# append the nested list at the end
my_list.append([5, 8, 'Tom', 7.5, 'Emma'])
print(my_list) # Output [5, 8, 'Tom', 7.5, 'Emma', [5, 8, 'Tom', 7.5, 'Emma']]
print(my_list[-1])

# Add item at the specified position in the list
# Using insert()
# insert 25 at position 2
my_list.insert(2, 25)
print(my_list) # [5, 8, 25, 'Tom', 7.5, 'Emma', [5, 8, 'Tom', 7.5, 'Emma']]

# insert nested list at position 3
my_list.insert(3, [25, 50, 75])
print(my_list) # [5, 8, 25, [25, 50, 75], 'Tom', 7.5, 'Emma', [5, 8, 'Tom', 7.5, 'Emma']]

# Using extend()
my_list.extend([25, 75, 100])
print(my_list) # [5, 8, 25, [25, 50, 75], 'Tom', 7.5, 'Emma', [5, 8, 'Tom', 7.5, 'Emma'], 25, 75, 100]

# concat list
new_list = list (['Todo1', 'Todo2', 'Todo3'])
contact_list = new_list + my_list
print(contact_list) # ['Todo1', 'Todo2', 'Todo3', 5, 8, 25, [25, 50, 75], 'Tom', 7.5, 'Emma', [5, 8, 'Tom', 7.5, 'Emma'], 25, 75, 100]

# modify all items
my_list_all = list([2, 4, 6, 8])

for i in range (len(my_list_all)):
    #calculate square of each number
    square = my_list_all[i] * my_list_all[i]
    my_list_all[i] = square

print(my_list_all)

# Removing elements from a List
my_list_remove = list([2, 4, 6, 8, 10, 12, 6, 6, 6])

# remove item 6 (first element found)
my_list_remove.remove(6)
# remove item 8 (first element found)
my_list_remove.remove(8)

print(my_list_remove) # [2, 4, 10, 12, 6, 6, 6]

# Remove all occurrence of a specific item
# for item in my_list_remove:
#     my_list_remove.remove(6)

# print(my_list_remove)


my_list = list([6, 4, 6, 6, 8, 12])

for item in my_list:
    my_list.remove(6)

print(my_list) # [4, 8, 12]
# Output [4, 8, 12]

# Remove item present at given index
# remove item present at index 2
my_list.pop(2)
print(my_list) # [4, 8] Delete 12 because the current list is [4, 8, 12]

# remove item without passing index number
my_list.pop()
print(my_list) # [4, 8] Delete 8 because the current list is [4, 8]
