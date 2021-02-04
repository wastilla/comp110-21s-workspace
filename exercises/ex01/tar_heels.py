"""An exercise in remainders and boolean logic."""

__author__ = "730387741"


# Begin your solution here...
number = input("Enter an int: ")
number = int(number)
if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
else:
    if number % 7 == 0:
        print("HEELS")
    else:
        if number % 2 == 0:
            print("TAR")
        else:
            print("CAROLINA")