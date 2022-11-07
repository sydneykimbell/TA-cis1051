# initialize list

fruits = ['apple', 'banana', 'cherry']

print(fruits)


# use len() function to get list length

length = len(fruits)
print(length)

# lists can contain any data types

nums = [1, 3 , 17, 1, 9]
data = [True, False, False, True]

# a list can contain multiple data types

values = [1, 'apple', True]

# can also use list() constructor to initialize a list

animals = list(("dog", "cat", "snake"))

# you can use indexes to find values in a list 
# use [] for list indexing

example = animals[0]
print(example) # prints 'dog', the 0th entry in the list

# lists are mutable, meaning that elements in a list can be changed after a list is initialized

animals[1] = 'chinchilla'
print(animals)
