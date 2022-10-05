import random

def get_num_trials():
    '''asks user for number of trials and returns the value'''
    trials = int(input('Enter the number of rolls: '))
    return trials


def roll():
    '''simulates rolling two dice and returns the sum of both rolls'''
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    res = die_1 + die_2
    return res

def main():

    # get the number of trials
    trials = get_num_trials()


    #initialize variables to count times each number is rolled
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    elevens = 0
    twelves = 0

    
    # simulate rolling the dice 
    for i in range(trials):
        res = roll()

        # using only simple primitive data types, count up the results
        if res == 2:
            twos += 1
        elif res == 3:
            threes += 1
        elif res == 4:
            fours += 1
        elif res == 5:
            fives += 1
        elif res == 6:
            sixes += 1
        elif res == 7:
            sevens += 1
        elif res == 8:
            eights += 1
        elif res == 9:
            nines += 1
        elif res == 10:
            tens += 1
        elif res == 11:
            elevens += 1
        else:
            twelves += 1

# output the results using a table. remember to use string formatters
# table must include 3 columns - 'Number', 'Rolls' (number of times the number is rolled), 'Percent' (proporition of times the number is rolled)