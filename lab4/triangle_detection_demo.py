# LAB 4 DEMO

# if statements

x = 10
y = 20

if x < y:
    print('x is less than y')

if x > y:
    print('x is greater than y')

a = 20
b = 20

# elif

if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')

c = 20
d = 30

# else

if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
else:
    print('c is less than d')

# and keyword

x = 100
y = 50
z = 200

if x > y and z > x:
    print('both conditions are true')

if x > y and x > z:
    print('both conditions are true')

# or keyword

if x > y or z > x:
    print('at least one of the conditions is true')

if x > y or x > z:
    print('at least one of the conditions is true')

if y > x or x == y:
    print('at least one of the conditions is true')

# nested if statements

num = 50

if num > 10:
    print('num is greater than 10')
    if num > 20:
        print('num is greater than 20')
    else:
        print('num is not greater than 20')

if num >= 0:
    if num == 0:
        print('num is equal to zero')
    else:
        print('num is positive')
else:
    print('num is negative')
