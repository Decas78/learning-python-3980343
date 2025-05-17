#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
# today = date.today()
# print("Todays date is:", today)
# print(f'Date Components: {today.day} {today.month} {today.year} ')

# # print out the date's individual components
# print("Today's weekday number:", today.weekday())




# retrieve today's weekday (0=Monday, 6=Sunday)

# days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# print("Which is a", days[today.weekday()])


## DATETIME OBJECTS
# Get today's date from the datetime class

today = datetime.now()
print("The current date and time is: ", today)


# Get the current time

t = datetime.time(datetime.now())
print(t)