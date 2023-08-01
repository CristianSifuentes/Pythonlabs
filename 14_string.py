text = 'Ella sabe programar en Python'
print('JavaScript' in text) # False
print('Python' in text) # True
if 'JS' in text:
    print('Elegiste bien')
else:
    print('Tambien elegiste bien') 

size = len('amor  werwer  ')
print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('P'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Python'))
print(text.replace('Python', 'Go')) # programar

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) # Este es un titulo
print(text_2.title()) # Este Es Un Titulo
print(text_2.isdigit()) # False
print('398'.isdigit())