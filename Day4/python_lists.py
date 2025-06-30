# Lists a Data Structure

# Connected data

#fruits = [item1, item2]

fruits = ["cherry", "apple", "pear"]

# Selecting an item from the list
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Changing the List
fruits[0] = "Cherry"
print(fruits)

# Appending to a list
fruits.append("Banana")
print(fruits)

# Extending a list
fruits.extend(["Dates", "Watermelon", "Strawberry"])
print(fruits)

# Removing 
fruits.pop()
print(fruits)