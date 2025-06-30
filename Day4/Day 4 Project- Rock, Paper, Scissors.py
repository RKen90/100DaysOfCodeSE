'''
What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors

Computer Chose

You Win/Lose

'''
import random

number = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors ")
number = int(number)
# print(type(number))


options = ["Rock", "Paper", "Scissors"]
random_options = random.choice(options)
# print(random_options)

if number == 0:
   print("You Chose Rock")
   if random_options == "Rock":
       print(f'Computer chose {random_options}')
       print("Draw, try again")
   elif random_options == "Paper":
       print(f'Computer chose {random_options}')
       print("You lose!")
   else:
       print(f'Computer chose {random_options}')       
       print("You win!")
elif number == 1:
   print("You Chose Paper")
   if random_options == "Rock":
       print(f'Computer chose {random_options}')       
       print("You win!")
   elif random_options == "Paper":
       print(f'Computer chose {random_options}')
       print("Draw, try again")
   else:
       print(f'Computer chose {random_options}')
       print("You lose!")
elif number == 2:
    print("You chose Scissors")
    if random_options == "Rock":
       print(f'Computer chose {random_options}')
       print("You lose!")
    elif random_options == "Paper":
       print(f'Computer chose {random_options}')
       print("You win!")
    else:
       print(f'Computer chose {random_options}')
       print("Draw, try again!")
else:
    print("Please enter a valid number")