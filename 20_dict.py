person = {"name": "Jessa", 'country': "USA", "telephone": 1178, "lang": ['python', 'javascript']}

# update dictionary by adding 2 new keys
person["weight"] = 50
person.update({"height": 6})

# pass new keys as as list of tuple
person.update([("city","Texas"), ("company", "Google")])
print(person) # {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'lang': ['python', 'javascript'], 'weight': 50, 'height': 6, 'city': 'Texas', 'company': 'Google'}

# print the updated dictionary
print(person) #  {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

person["height"] -= 2
print(person) # {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 4}

person["lang"].append(' Robert')
print(person) 
# {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'lang': ['python', 'javascript', ' Robert'], 'weight': 50, 'height': 4}

del person['country']
print(person) # {'name': 'Jessa', 'telephone': 1178, 'lang': ['python', 'javascript', ' Robert'], 'weight': 50, 'height': 4}

person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

# set default value if key doesn't exists
person_details.setdefault('state', 'Texas')
print(person_details)# {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'state': 'Texas'}

# key doesn't and value not mentioned.default None
person_details.setdefault("zip")
print(person_details)#{'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'state': 'Texas', 'zip': None}

# key exists and value mentioned. doesn't  change value
person_details.setdefault('country', 'Canada')
print(person_details)# {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'state': 'Texas', 'zip': None}

#person_details.pop()
#print(person_details) # TypeError: pop expected at least 1 argument, got 0

person_details.pop('name')
print(person_details) # {'country': 'USA', 'telephone': 1178, 'state': 'Texas', 'zip': None}

print(person_details.items())
# dict_items([('country', 'USA'), ('telephone', 1178), ('state', 'Texas'), ('zip', None)])

print(person_details.keys()) 
# dict_keys(['country', 'telephone', 'state', 'zip'])

print(person_details.values()) # dict_values(['USA', 1178, 'Texas', None])

# Removing items from the dictionary

'''
pop(key[,d])	Return and removes the item with the key and return its value. If the key is not found, it raises KeyError.
popitem()	Return and removes the last inserted item from the dictionary. If the dictionary is empty, it raises KeyError.
del key	The del keyword will delete the item with the key that is passed
clear()	Removes all items from the dictionary. Empty the dictionary
del dict_name	Delete the entire dictionary

'''

person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}
