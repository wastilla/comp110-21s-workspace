"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730387741"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Generates a random integer from 1 to 4 and prints the fortune associated with the integer"""
    fortune = (randint(1, 4))
    if fortune == 1:
        return("A beautiful, smart, and loving person will be coming into your life")
    else:   
        if fortune == 2:
            return("Your life will be happy and peaceful.")
        else:
            if fortune == 3:
                return("Soon life will become more interesting.")
            else: 
                if fortune == 4:
                    return("You're gonna have a great day today.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
