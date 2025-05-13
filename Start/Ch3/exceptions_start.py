# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:

# x = 10 / 0
# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together

# try:
#   x = 10 / 0
# except:
#   print("Didnt work mate")

# You can also catch specific exceptions
try:
  answer = input("What Should I Divide 10 by?")
  num = int(answer)
  print(10/num)
except ValueError as e:
  print("Incorrect Value for Division")
except ZeroDivisionError as e:
  print("Sorry but you cant divide by zero")
finally:
  print("Finally always runs")
