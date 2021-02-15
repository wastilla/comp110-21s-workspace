"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730387741"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population, doses, doses_per_day, target)
    date: int = future_date(days)
    target = round(target)
    days = round(days)
    target = str(target)
    days = str(days)
    date = str(date)
    print("We will reach " + target + "% vaccination in " + days + " days, which falls on " + date + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Function calculates the number of days until target is reached."""
    target = target / 100
    target_population = population * target
    pop_with_vaccine: float = doses / 2
    days: float = ((target_population - pop_with_vaccine) * 2) / doses_per_day
    return int(days)


def future_date(days: int) -> str:
    """Function calculated the date target will be reached."""
    today: datetime = datetime.today()
    number_of_days: timedelta = timedelta(days)
    target_date: datetime = today + number_of_days
    target_date = target_date.strftime("%B %d, %Y")
    return str(target_date)


if __name__ == "__main__":
    main()
