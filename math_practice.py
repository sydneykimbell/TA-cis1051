import math
# formulas in python

# a.) fahrenheit to celcius

f = 72

c = (5/9) * (f-32)

print('Temperature in C: ', c)

# b.) loan payment

n = 120
a = 100000
r = 0.04

payment = (r*a)/(1-(math.pow((1+r), -n)))

print('Payment: ', payment)

# c.) calculating two roots of a quadratic equation

a = 1
b = 4
c = 3

root1 = (-b + math.sqrt(math.pow(b,2)-(4*a*c))) / (2*a)
root2 = (-b - math.sqrt(math.pow(b,2)-(4*a*c))) / (2*a)

print('root 1: ', root1, '\nroot2: ', root2)

# d.) distance formula

x1 = 9
y1 = 9
x2 = -7
y2 = 1

d = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print('distance: ', d)

# e.) haversine function used in maritime navigation

theta = 35

haversine = (1 - math.cos(math.radians(35))) / 2

print('haversine: ', haversine)
