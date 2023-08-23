# function
def message():
    print("Welcome to PYnative")

# call function using its name
message()



# function
def course_func(name, course_name):
    print("Hello", name, "Welcome to PYnative")
    print("Your course name is", course_name)

# call function
course_func('John', 'Python')


# function
def calculator(a, b):
    add = a + b
    # return the addition
    return add

# call function
# take return value in variable
res = calculator(20, 5)

print("Addition :", res)
# Output Addition : 25



# function
def even_odd(n):
    # check numne ris even or odd
    if n % 2 == 0:
        print('Even number')
    else:
        print('Odd Number')

# calling function by its name
even_odd(19)
# Output Odd Number



# import randint function
from random import randint

# call randint function to get random number
print(randint(10, 20))
# Output 14


# Single-Line Docstring

def factorial(x):
    """This function returns the factorial of a given number."""
    return x

# access doc string
print(factorial.__doc__)

print(help(factorial))

# Multi-Line Docstring

def any_fun(parameter1):
    """              
    Description of function
                    
    Arguments:   
    parameter1(int):Description of parameter1
                    
    Returns:      
    int value     
    """              
print(any_fun.__doc__)

# Return Value From a Function

def is_even(list1):
    even_num = []
    for n in list1:
        if n % 2 == 0:
            even_num.append(n)
    # return a list
    return even_num

# Pass list to the function
even_num = is_even([2, 3, 42, 51, 62, 70, 5, 9])
print("Even numbers are:", even_num)