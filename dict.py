person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

'''
Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
Eliminar el elemento del diccionario con la llave "age".
Imprimir una lista con las llaves del diccionario.
Imprimir una lista con los valores del diccionario.

'''
person["twitter"] = '@nicobytes'
print(person)

person["name"] = 'Felipe'
print(person) # {'name': 'Felipe', 'lastName': 'Molina', 'age': 29, 'twitter': '@nicobytes'}

del person['age']
print(person) # {'name': 'Felipe', 'lastName': 'Molina', 'twitter': '@nicobytes'}

print(person.keys()) # dict_keys(['name', 'lastName', 'twitter'])

print(person.values()) # dict_values(['Felipe', 'Molina', '@nicobytes'])

# person["twitter"] = "@nicobytes"
# person["name"] = 'Felipe'
# person.pop('age')
# print(list(person.keys())) # en platzi marca error sin colocar la list
# print(list(person.values()))  en platzi marca error sin colocar la list



