import random

# for loops

for i in range(5):
    print('Hello!', i)

for i in range(2,6):
    print('Goodbye!', i)

for i in range(5):
    for j in range(2):
        print('i = ', i, 'j = ', j)

for i in range(1, 10, 5):
    print(i)

# simulations

trials = 100000
heads = 0
tails = 0

for i in range(trials):
    coin  = random.randint(0,1)
    if coin == 0:
        heads += 1
    else:
        tails += 1

print('number of heads:', heads)
print('number of tails:', tails)
print('probability of heads:', heads/trials)
print('probability of tails:', tails/trials)

# tabular string formatting

print('{:<10} {:<10} {:<20} {:<20}'.format('heads', 'tails', 'percent heads', 'percent tails'))
print('{:<10} {:<10} {:<20} {:<20}'.format(heads, tails, heads/trials, tails/trials))

# probability

marbles = ['blue', 'blue', 'red', 'green', 'green', 'green', 'yellow']

blue = 0
red = 0
green = 0
yellow = 0

for marble in marbles:
    if marble == 'blue':
        blue += 1
    elif marble == 'red':
        red += 1
    elif marble == 'green':
        green += 1
    else:
        yellow += 1

sample_space = len(marbles)

p_blue = blue/sample_space
p_red = red/sample_space
p_green = green/sample_space
p_yellow = yellow/sample_space

print('P(blue) =', p_blue)
print('P(red) =', p_red)
print('P(green) =', p_green)
print('P(yellow) =', p_yellow)

print('sum of probabilities:',p_blue + p_red + p_green + p_yellow)
