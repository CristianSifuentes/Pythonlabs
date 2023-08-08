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