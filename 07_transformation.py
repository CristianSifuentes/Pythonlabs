# Casting float value to an integer

pi = 3.14 # float number
print(type(pi))
# Output class 'float'

# converting float integer
num = int(pi)
print("Integer number :", num)
# Output 3
print(type(num))
# Output class 'int'

# Casting Boolean value to an integer
flag_true = True
flag_false = False
print(type(flag_true))
# Output class 'bool'

# converting boolean to integer
num1 = int(flag_true)
num2 = int(flag_false)

print("Integer number 1: =>", num1)
# Output 1
print(type(num1))
# Output class 'int'

print("Integer number 2: =>", num2)
# 0
print(type(num2))
#  class 'int'


# Casting a string to an integer
string_num = "225"
print(type(string_num))
# Output class 'str'

# converting str to integer
num1 = int(string_num)

print("Integer number 1:", num1)
# Output 225
print(type(num1))
# Output class 'int'

