# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = ["apples", "oranges", "bananas", 4, False]
print(len(mylist))

# to access a member of a sequence type, use []

# print(mylist[0])
# print(mylist[-2])
# mylist[3] = 23
# print(mylist[3])

# add a list to another list
# second_list = [4, 9, 10]
# mylist = mylist + second_list
# print(mylist)

# print(mylist[0][4])


# use slices to get parts of a sequence
print(mylist[1:-1:2])

# you can use slices to reverse a sequence
print(mylist[::-1])

# Tuples are like lists, but they are immutable
# Immutable which means they are more efficient and used when you dont need values to change
# Can be used in a function to return multiple values
mytuple = (0,1,2,"three")
print(mytuple)

# Sets are also sequences, but they contain unique values (cannot contain duplicates)
# Used to ensure theres only one instance of each value

myset = {1,2,3,2,4, "hey"}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership

print(1 in mylist)
print(2 in mytuple)
print(5 in myset)