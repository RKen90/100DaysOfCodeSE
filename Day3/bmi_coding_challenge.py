'''
BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:



'''
print("Welcome to the BMI Calculator fatass!")
weight = int(input("What is your weight is KG? "))
height = float(input("What is your height in M? "))


bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Underweight")
elif bmi <25:
    print(f"Your BMI is {bmi}, you are a Normal weight")
else:
    print(f"Your BMI is {bmi}, you are Overweight")
    
'''    
if bmi < 18.5:
    print("underweight")
elif bmi <25:
    print("normal weight")
else:
    print("overweight")    
# 🚨 Do not modify the values above
# Write your code below 👇
'''