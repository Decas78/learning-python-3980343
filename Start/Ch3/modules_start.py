# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# import the math module, which contains features for working with mathematics
import math

print("the square root of 16 =", math.sqrt(16))

# import a specific part of the module so you can refer to it more easily
from math import pi
print(pi)

# import a module and give it a different name
import numpy as np


# the math module contains lots of pre-built functions
import random as rand



# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200
r = rand.randint(100,1000)

# Use the 3rd party tabulate module to print tabulated data:
from tabulate import tabulate
# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table

print(tabulate(data, headers="firstrow", tablefmt="heavy_grid"))