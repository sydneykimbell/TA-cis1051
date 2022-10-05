# LAB 2 DEMO

# user input

num = input('Enter a number: ')
print('Your number is', num)

name = input('Enter your name: ')
age = input('Enter your age: ')
print('Your name is', name, 'and your age is', age)

# output using .format

example = 'Your name is {name} and your age is {age}'.format(name = name, age = age)
print(example)
example = 'Your name is {0} and your age is {1}'.format(name, age)
print(example)
example = 'Your name is {} and your age is {}'.format(name, age)

# importing modules

#print(math.pi) - does not work when math module is not imported
#demonstrate from math import pi

import math
print(math.pi)

print(dir(math))

cos = math.cos(0.5)
print('The cosine of 1/2 is', cos)

cos2 = math.cos((math.pi)/2)
print('The cosine of pi/2 is', cos2)

print('4 factorial is equal to', math.factorial(4))

pow_ex = math.pow(2,5)
print(pow_ex)

print(math.sqrt(33))

e = math.e
pi = math.pi
print('e:', e, '\npi:', pi)

# distance formula solution

x1 = 9
y1 = 9
x2 = -7
y2 = 1
d = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
print(d)

# mad libs example
# https://www.madtakes.com/libs/188.html

noun = input('Enter a noun: ')
plural_noun = input('Enter a plural noun: ')
noun2 = input('Enter a noun: ')
place = input('Enter a place: ')
adjective = input('Enter an adjective: ')
noun3 = input('Enter a noun: ')
number = int(input('Enter a number: '))

print('Be kind to your' + noun + '-footed', plural_noun)
print("For a duck may be somebody's", noun2)
print('Be kind to your', plural_noun, 'in', place)
print('Where the weather is always', adjective)
print('You may think that this is the', noun3)
print('Well it is.')
print('The square root of', number, 'is', str(math.sqrt(number)))

# mad libs line using .format

print('Be kind to your {}-footed {}'.format(noun, plural_noun))
