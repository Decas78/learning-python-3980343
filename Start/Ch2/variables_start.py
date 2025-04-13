# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print(myint, "\n", myfloat, mystr, mybool)

# Operators are used to perform operations on variables
print(myint % 4)

another_str = " ANOTHER ONE"
print(mystr + another_str)

# Logical and comparison operators 
print(myint == myfloat)

print(myint < 20 or myfloat > 100)
print(not(myint < 20 or myfloat > 100))

# re-declaring a variable works

myint=33

print(myint)