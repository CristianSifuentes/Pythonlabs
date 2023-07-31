# If statement in Python

number = 6
if number > 5:
    # Calculate square
    print(number * number)
print('Next  lines of code')

password = input('Enter password ')
if password == "PYnative@#29":
    print("Correct password")
else:
    print("Incorrect Password")


'''
Chain multiple if statement in Python

'''

def user_check(choice):
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)

# Chain multiple if statement in Python
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is grater than', num2)
else:
    print(num1, 'is smaller than', num2)


'''
Par o impar

'''
number = int(input('Ingrese un numero => '))
result = number % 2
if(result == 0):
    print('Es par')
else:
    print('Es impar')