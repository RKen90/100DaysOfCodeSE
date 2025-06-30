print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
size = size.lower()
pepperoni = input("Do you want peperroni on your pizza? Y or N ")
pepperoni = pepperoni.lower()
extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese = extra_cheese.lower()

'''
Small = 15
Medium = 20
Large = 25
Pepperoni = 2
Cheese = 1
'''
bill = 0

if size == 's':
    bill = 15
    print(f"This Pizza costs £{bill}")
elif size == 'm':
    bill = 20
    print(f"This Pizza costs £{bill}")
else:
    bill = 25
    print(f"This Pizza costs £{bill}")
if pepperoni == 'y':
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == 'y':
    print("Extra Cheese costs £1")
    bill += 1
print(f"The total cost of your pizza is £{bill}")