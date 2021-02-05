"""A vaccination calculator."""

__author__ = "730387741"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_pr: int = int(input("Target percent vaccinated: "))

target_pr = target_pr / 100

target_population = population * target_pr
pop_with_vaccine: float = doses_administered / 2
days: float = ((target_population - pop_with_vaccine) * 2) / doses_per_day
print(days)

today: datetime = datetime.today()
number_of_days: timedelta = timedelta(days)
target_date: datetime = today + number_of_days
target_date = target_date.strftime("%B %d, %Y")

target_pr = target_pr * 100
target_pr = round(target_pr)
days = round(days)
target_pr = str(target_pr)
days = str(days)
target_date = str(target_date)

print("We will reach " + target_pr + "% vaccination in " + days + " days, which falls on " + target_date + ".")