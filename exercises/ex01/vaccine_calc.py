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
population = input("Population: ")
doses_administered = input("Doses administered: ")
doses_per_day = input("Doses per day: ")
target_percent = input("Target percent vaccinated: ")

population = int(population)
doses_administered = int(doses_administered)
doses_per_day = int(doses_per_day)
target_percent = int(target_percent)/100

target_population = population * target_percent
pop_without_vaccine = population - (doses_administered/2)
days_until_target = ((pop_without_vaccine - target_population)*2)/doses_per_day

today: datetime = datetime.today()
number_of_days: timedelta = timedelta(days_until_target)
target_date: datetime = today + number_of_days
target_date = target_date.strftime("%B %d, %Y")

target_percent = target_percent * 100
target_percent = round(target_percent)
days_until_target = round(days_until_target)
target_percent = str(target_percent)
days_until_target = str(days_until_target)
target_date = str(target_date)

print("We will reach " + target_percent + "% vaccination in " + days_until_target + " days, which falls on " + target_date  + ".")


