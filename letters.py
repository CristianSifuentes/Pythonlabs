letters = ['A', 'B', 'C', 'D', 'E', 'F']

'''
Agregar la letra G al final de la lista.
Reemplazar la letra en la posición 0 con la letra Z.
Eliminar la letra C de la lista.
Imprimir la lista resultante al revés.
'''

# Escribe tu solución 👇
letters.append('G')
print(letters)

letters[0] = 'Z'
print(letters)

letters.remove('C')
print(letters)

letters.reverse()
print(letters)

