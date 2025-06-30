'''
The Modulo

Modulo Operator - %
10 % 5 = 0
Gives the remainder
'''

print(10 % 5)
print(10 % 3)
print(10 % 4)


# Coding Challenge
# Check if the number inputted by the user is odd or even

number = input("Please enter a number ")
number = int(number)


if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is as odd as you!")