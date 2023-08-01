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

# Remove the range of items
my_list = list([2, 4, 6, 8, 10, 12])
# remove range of items
# remove item from index 2 to 5
del my_list[2:5]
print(my_list) # [2, 4, 12] because start in '6' and finish in '10' deleting 5 elements 

# remove all items starting from index 3
my_list = list([2, 4, 6, 8, 10, 12])
del my_list[3:]
print(my_list) # [2, 4, 6]

my_list.reverse()
print(my_list)  # [2, 4, 6]

# sort in numbers
numbers_a = [1, 3, 2, 6, 7, 4, 5]
numbers_a.sort()
print(numbers_a) # [1, 2, 3, 4, 5, 6, 7]

# sort in string
strings = ['a', 'b', 'e', 'c', 'd']
strings.sort()
print(strings) # ['a', 'b', 'c', 'd', 'e'] validate how it´s work usings "Strings"

# in heterogeneous list dont work sort


''''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''