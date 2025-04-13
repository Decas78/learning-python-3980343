# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function


def what_name():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

# function that takes parameters
def what_name_param(greeting):
  print("hello world!")
  name = input("What is your name? ")
  print(greeting, name)

# what_name_param("G'day")
# what_name_param("How are you doing today")

# function that returns a value

def add(num1, num2):
  return num1 + num2

print(add(1, 5))

def cube(x):
  return x*x*x
print(cube(10))

# function with default value for an parameter

def hello_func(greeting, name=None):
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)

hello_func("Nice to meet ya")
# function with variable number of parameters

def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result

print(multi_add(5, 9, 10, 555))
