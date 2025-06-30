'''
Banker Roulette

you are to look through this friends list and you're going to write some code using what you've learned

about randomization in Python, and also lists in Python to be able to print out a random, one of these

names.
'''
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[3])
# print(friends[4])

randomFriend = random.randint(0, 4)

print(f'The person who should pay the bill is {friends[randomFriend]}')



# Using Random.choice

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[3])
# print(friends[4])

randomFriend = random.choice(friends)

print(f'The person who should pay the bill is {randomFriend}')
