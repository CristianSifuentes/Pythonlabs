import random

def choice(a):
    if a == 1:
        return ('Rock')
    elif a == 2:
        return('Paper')
    elif a == 3:
        return ('Scissor')
    else:
        return ('Lost')

def tex():
    print(f'\nHas elegido : { choice(usuario)}')
    print(f'\nEl PC ha elegico: {choice(pc)}\n')


print(f'\nJuego de piedra, papel o tijeran\n')
usuario = int(input('ingrese \n1 para Rock \n2 para Paper \n3 para Tijeras =>'))
pc = random.randint(1,3)
if pc == usuario:
    tex()
    print('Empate')
elif((usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2)):
    tex()
    print('You win')
elif usuario not in range(1, 2):
    tex()
    print('Looser')
else:
    tex()
    print('Has perdido')
