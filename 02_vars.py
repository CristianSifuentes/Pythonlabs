# Creating a variable


my_name = "cristian" # string assignment
print(my_name) # cristian
print(type(my_name)) # <class 'str'>

my_age = 18 # integer assignment
print(my_name) # 18
print(type(my_age)) # <class 'int'>

print("my age => ", my_age) # my age =>  18

my_salary = input("Whats is your daily salary? ") # Whats is your daily salary? 
print("your salary month salary is => ", (my_salary * 30))  # your salary month salary is => 

#fix problem
month_salary = float(my_salary) * 30 # float assignment
print("your salary month salary is => ", month_salary) # your salary month salary is => 
print(type(month_salary)) # <class 'float'>


# Changing the value of a variable

var = 10
print(var)  # 10
# print its type
print(type(var))  # <class 'int'>

# assign different integer value to var
var = 55
print(var)  # 55

# change var to string
var = "Now I'm a string"
print(var)  # Now I'm a string
# print its type
print(type(var))  # <class 'str'>

# change var to float
var = 35.69
print(var)  # 35.69
# print its type
print(type(var))  # <class 'float'>


