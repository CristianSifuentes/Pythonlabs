# and (Logical and)
'''
The logical and operator returns 
True if both expressions are True.
 Otherwise, it will return. False.

'''

print(True and False) # False
# both are True
print(True and True) # True
print(False and False) # True
print(False  and True) # True

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")

# Arithmetic values
# Logical and always returns the second value

print(10 and 20) # 20
print(10 and 5) # 5
print(100 and 300) # 300

# or (Logical or)
'''
The logical or the operator returns a 
boolean  True if one expression is true, 
and it returns False if both values are 
false.

'''

print(True or False) # True
print(True or True) # True
print(False or False) # false 
print(False or True) # True

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 or b < 0:
    # at least one expression is true so conditions is true
    print(a + b) # 6
else:
    print("Do nothing")

# Arithmetic value
# Logical or it always returns the first value; as a result, see the following code.

print(10 or 10) # 10
print(10 or 5) # 10
print(100 or 300) # 100

