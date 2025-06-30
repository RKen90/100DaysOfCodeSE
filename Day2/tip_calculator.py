'''
Welcome to the tip calculator! ✅
What was the total bill? $xxx ✅
How much tip would you like to give? 10, 12, or 15?
How many people split the bill? x
Each person should pay: yy

Percentage Conversion = 12% = 12/100 


bill * tip / people
'''

print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
bill = float(bill)
# print(bill)
#print(type(bill))
tip = input("How much tip would you like to give? 10, 12 or 15? ")
tip = int(tip)
tip_percent = tip / 100
#print(tip_percent)
#print(tip_percent * bill)
#print(bill * tip_percent)
#print(tip)
#print(type(tip))
people = input("How many people split the bill? ")
people = int(people)

total = (bill + (bill * tip_percent)) / people
print(f"The amount each person should pay is {total:.2f}")