#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it

# print(timedelta(days=365, hours=5, minutes=1))

# print today's date

# now = datetime.now()
# print("Today is ", now)

# # print today's date one year from now

# print("In one year it will be ", now + timedelta(days=365))

# # create a timedelta that uses more than one argument
# print("In two weeks and 4 days it will be ", now + timedelta(weeks=2, days=4))

# # calculate the date 1 week ago, formatted as a string

# OneWeekAgo = (now - timedelta(weeks=1))
# OneWeekAgoFormat = OneWeekAgo.strftime("%a, %d %B, %Y")
# print(OneWeekAgoFormat)

### How many days until April Fools' Day?

today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
  print(f"April fools day already went by {(today-afd).days} days ago")
  afd = afd.replace(year=today.year+1)

time_to_afd = afd-today
print(f"its just {time_to_afd.days} days until April Fools' Day")