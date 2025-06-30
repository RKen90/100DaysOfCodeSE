'''
Randomisation
'''

import random

#Random Integers
print(random.randint(0, 10))


''' 
What is a Python Module

Splitting the code up into different sections (preventing excessive length)
We can call the module (like import random)
Compartmentalisation

Creating a module
'''

import myModule

print(myModule.myNumber)


# Random.random

random_number = random.random() 
print(random_number)
random_number = random.random() * 10
print(random_number)



# Random Floating Point Number
print(random.uniform(1, 10))