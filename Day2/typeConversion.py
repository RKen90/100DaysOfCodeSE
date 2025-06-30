'''
Type Error, Type Checking, Type Conversion 
'''

# Type Checking
print(type("Hello"))
print(type(123))
print(type(1.2345))
print(type(False))

# Type Conversion
print("123" + "456")
print(int("123")+ int("456"))

# We can convert to any data type
int()
float()
str()
bool()

# print("Number of letters in your name: " + len(input("Enter your name ")))

name = input("Enter your name ")
print(type(name))
digits = len(name)

print("Number of letters in your name " + str(digits))