count = 1
# condition: Run llop till count is less than 3
while count < 3:
    print(count)
    count = count + 1

count = 0
number = 180
while number > 10:
    # divide number by 3
    number = number / 3
    # increase count
    count = count + 1

print('Total iteration required', count)


i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j, end='')
        j = j + 1
    i = i + 1
    print()    

'''
12345678910
12345678910
12345678910
12345678910
12345678910
'''

# for loop inside While loop
print('Show perfect number from 1 to 100')
n = 2
# outer while loop
while n <= 100:
    x_sum = 0
    # inner for loop
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Perfect number:', n)
    n += 1