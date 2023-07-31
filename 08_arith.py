# + (Addition)
x = 10
y = 40
print(x + y)
# Output 50

name = "Kelly"
surname = "Ault"
print(surname + " " + name)
# Output Ault Kelly

# - (Subtraction)
x = 10
y = 40
print(y - x)
# Output 30


# * (Multiplication)
x = 2
y = 4
z = 5
print(x * y)
# Output 8 (2*4)
print(x*y*z)
# Output 40 (2*4*5)


name = "Jessa"
print(name * 3)
# Output JessaJessaJessa

# / (Division)
x = 2
y = 4
z = 8

print(y / x)
# Output 2.0
print(z / y / x)
# Output 1.0
#print(z / 0)  # error
#ZeroDivisionError

# // Floor division)
x = 2
y = 4
z = 2.2

# normal division
print(y / x)
# Output 2.0

# floor division to get result as integer
print(y // 2)
# Output 2

# normal division
print(y / z)  # 1.81

# floor division.
# Result as float because one argument is float
print(y // z)  # 1.0


# ℅ (Modulus)
x = 15
y = 4

# 15 / 4 = 3.75
print(x % y)
# Output 3

# ** (Exponentiation)
num = 2
# 2*2
print(num**2)
# Output 4

# 2*2*2
print(num**3)
# Output 8

print(" => : ", 2 ** 3 + 3 - 7 / 1 // 4)

'''
P - Paréntesis
E - Exponentes
M - Multiplicación
D - División
A - Adición
S - Sustracción
'''
# P 
print(2 ** 3) # 8
print(8 + 3 - 7 / 1 // 4)
# D 
print(7 / 1 // 4) # 1.0
print(8 + 3 - 1.0)
# A
print(11 - 1.0)
# S
print(11 - 1.0)



