for num in range(10):     
    print(num)

sum = 0
for i in range(2, 22, 2):
    sum = sum + i
    #print(i)

# range(inicia, termina, aumento)
print(sum)

numbers = [1, 2, 3, 4, 5]
# iterate over each element in list num
for i in numbers:
    # ** exponent operator
    square = i ** 2
    print("Square of:", i, "is:", square)

'''
Square of: 1 is: 1
Square of: 2 is: 4
Square of: 3 is: 9
Square of: 4 is: 16
Square of: 5 is: 25
'''


# tuple
number_tuple = (10, 20, 25.75, 10, 20,25.75 )

for element in number_tuple:
    print(element)

'''
10
20
25.75
10
20
25.75
'''

# dict
person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178
}
for key in person:
    print(key, '=>', person[key])

'''
name => Jessa
country => USA
telephone => 1178
'''

for key, value in person.items():
    print(key, '=>', value)

'''
name => Jessa
country => USA
telephone => 1178
'''

people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

for person in people:
    print(person)

'''
{'name': 'nico', 'age': 34}
{'name': 'zule', 'age': 45}
{'name': 'santi', 'age': 4}
'''

for person in people:
    print('name =>', person['name'])

'''
name => nico
name => zule
name => santi
'''


for i in range(1, 11):
    if i % 2 == 0:
        print('Even Number :', i)
    else:
        print('Odd Number :', i)
'''
Odd Number : 1
Even Number : 2
Odd Number : 3
Even Number : 4
Odd Number : 5
Even Number : 6
Odd Number : 7
Even Number : 8
Odd Number : 9
Even Number : 10
'''

numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in numbers:
    if i > 15:
        # breake the loop
        break
    else:
        print(i)
'''
1
4
7
8
15
'''