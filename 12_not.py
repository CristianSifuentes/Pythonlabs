# not (Logical not)
# The logical not operator returns boolean True if the expression is false.

print(not False) # True return complements result
print(not True) # True return complements result

# actual use in code
a = True

# Logical not
if not a:
    # a is True so expression is False
    print(" xxx > ", a)
else:
    print("Do nothing")


# In the case of arithmetic values, Logical not always return False for nonzero value.
print(not 10) # False. Non-zero value
print(not 1)  # True. Non-zero value
print(not 5)  # False. Non-zero value
print(not 0)  # True. zero value

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <=1000))