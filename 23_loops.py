nestedlist = [[2,4,6,8,10],[1,3,5,7,9]]

print("Accessing the third element of the second list", nestedlist[1][2])
'''
0 => [2,4,6,8,10],
1 => [1,3,5,7,9]

nestedlist[1][2]

[
    1, => 0
    3, => 1
    5, => 2 (selected)
    7, => 3 
    9  => 4
]

'''
for i in nestedlist:
    print("list", i, "elements")

'''
list [2, 4, 6, 8, 10] elements
list [1, 3, 5, 7, 9] elements
'''

for i in nestedlist:
    print("list", i, "elements")
    for j in i:
        print(j)

'''
list [2, 4, 6, 8, 10] elements
2
4
6
8
10
list [1, 3, 5, 7, 9] elements
1
3
5
7
9
'''


# outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()


'''
range(start, stop, step)

Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

'''

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end="")
    print('')

'''
*
**
***
****
*****
'''

names = ['Kelly', 'Jessa', 'Emma']
# outer loop
for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()

'''
Kelly Kelly Kelly Kelly Kelly 
Jessa Jessa Jessa Jessa Jessa 
Emma Emma Emma Emma Emma 
'''

# Break Nested loop
for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)

'''
1 0
2 0
2 1
3 0
3 1
3 2
'''


# Continue Nested loop

first = [2, 4, 6]
second = [2, 4, 6]
for i in first:
    for j in second:
        if i == j:
            continue
        print(i, '*', j, '= ', i * j)

'''
2 * 4 =  8
2 * 6 =  12
4 * 2 =  8
4 * 6 =  24
6 * 2 =  12
6 * 4 =  24
'''

# Single Line Nested Loops Using List Comprehension
first = [2, 3, 4]
second = [2, 30, 40]
final  = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)
'''
[4, 32, 42, 5, 33, 43, 6, 34, 44]
'''

final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x != y]
print(final)
# [[10, 30], [10, 50], [20, 30], [20, 10], [20, 50], [30, 10], [30, 50]]

final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x == y]
print(final)
# [[10, 10], [30, 30]]