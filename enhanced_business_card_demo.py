# LAB 3 DEMO
import math
# creating functions

def example_function():
    print('Hello world!')

example_function()

# passing input to functions

def example_function2(input):
    print('Input:', input)

example_function('Hello')

# returning data

def squared(x):
    return x ** 2

y = squared(5)
print(y) # prints 25

def squared2(x):
    x ** 2

y = squared2(5)
print(y)

# using a function within a function

def pythag_thm(a, b):
    '''computes c in the pythagorean theorem given a and b
    a^2 + b^2 = c^2'''
    return math.sqrt(squared(a) + squared(b))

print(pythag_thm(3,4))

# scope of variables

g_var = 'Hello'

def example():
    print(g_var)

example()

def example2():
    l_var = 'goodbye'

#print(l_var) # error because l_var is not defined outside of the function

def example3():
    l_var = 'goodbye'
    return l_var

z = example3()
print(z)

total = 0

def sum(x, y):
    total = x + y
    print('Inside of function total: ', total)
    return total

sum(10,20)
print('Outside of function total: ', total)

total = sum(10,20)
print('After passing data total: ', total)

# constants

PI = 3.14
G = 9.8
print('pi: ', PI, '\n', 'g: ', G)