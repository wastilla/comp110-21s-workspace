"""EX03 - avoid_fifth function."""

__author__: str = "730387741"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("Will turn that bass down!"))

def avoid_fifth(y: str) -> str:
"""This function delets all e's from a string"""
    i: int = 0
    newString: str = ""
    temp: chr
    while i < len(y):
        temp = y[i]  
        if temp != "e" and temp != "E":
            newString += temp 
            i+=1
        else:
            i+=1
    return newString

        

if __name__ == "__main__":
    main()