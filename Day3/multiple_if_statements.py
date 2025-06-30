'''
Multiple IF Statements

'''


print("Welcome to the rollercoaster")

height = int(input("What is your height in CM? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Tickets are £12")
        bill = 12
    elif age >=12:
        print("Tickets are £7")
        bill = 7
    else:
        print("Tickets are £5")
        bill = 5
    photo = input("Do you want a photo? Y/N")
    photo = photo.lower()
    if photo == "y":
        bill += 3
        print(f"Your total bill is £{bill}")
    else:
        print(f"Your total bill is £{bill}")
        
    
else:
    print("Grow up you shortarse")