# create a dictionary using {}
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(person) # {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# create a dictionary using dict ()
person = dict({"name": "Jessa", "country": "USA", "telephone": 1178})
print(person)

# create a dictionary from sequence having each item as a pair
person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
print(person) # {'name': 'Mark', 'country': 'USA', 'telephone': 1178}

# create a dictionary with mixed keys keys
# first key is starting and second is an integer
sample_dict = { "name": "Jessa", 10: "Mobile" }
print(sample_dict) # {'name': 'Jessa', 10: 'Mobile'}

# create dictionary with value as a list
person = { "name": "Jessa", "telephones": [1423, 2355, 4234] }
print(person) # {'name': 'Jessa', 'telephones': [1423, 2355, 4234]}

#empty dictionary
emptydict = {}
print(type(emptydict)) # <class 'dict'>}

# Accessing elements of a dictionary
# create a dictionary named person
person = {
    "name": "Jessa",
    "country": "USA",
    "telephone": 1178
}

# len
print("len => ", len(person)) # len =>  3

# access value using key name in []
print(person['name']) # Output 'Jessa'
#print(person["SDASD"]) # KeyError: 'SDASD'

# get key value using key name in get()
print(person.get('telephone'))
# Output 1178

# Get all keys 
print(person.keys()) # dict_keys(['name', 'country', 'telephone'])

print(type(person.keys())) # <class 'dict_keys'>

# Get all values
print(person.values()) # dict_values(['Jessa', 'USA', 1178])

print(type(person.values())) # <class 'dict_values'>

# Get all key-value pair
print(person.items()) # dict_items([('name', 'Jessa'), ('country', 'USA'), ('telephone', 1178)])

print(type(person.items())) # <class 'dict_items'>

# Iterating a dictionary

# Iterating the dictionary using for-loop
print('key', ':',"value")
for key in person:
    print(key, ':', person[key])

'''
key : value
name : Jessa
country : USA
telephone : 1178
'''

# using items() method
print('key', ':', 'value')
for key_value in person.items():
    #first is key, and second is value
    print(key_value[0], key_value[1])

'''
key : value
name Jessa
country USA
telephone 1178
'''