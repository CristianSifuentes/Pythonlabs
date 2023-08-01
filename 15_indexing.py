# create a variable of type string
str = 'PYnative'

# prints complete string
print(str) # PYnative

# prints first character of the string
print(str[0]) # P

# prints characters starting from 2nd to 5th
print(str[2:6]) # nat

# length of string
print(len(str)) # 8

# concatenate string
print(str + "TEST") # PYnativeTEST

size = len(str)
print(str[size - 1]) # e
print(str[-1]) # e

text = '123456789'

# slicing
print(text[0:5]) # Ella (0 posición donde inicia, 5 numero de caracteres desde contando desde el inicio)
print(text[5:9]) # Inicia en 'P' termina en 'n' = 'Python'
print(text[:9]) # Si no se especifica empieza en 0, termina en 10, = 'Ella sabe '
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[5:9:1])
print(text[5:9:2])
print(text[5:9:2])
print(text[::])





