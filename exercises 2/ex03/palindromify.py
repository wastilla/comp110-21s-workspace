"""EX03 - palindromify function."""

__author__: str = "730387741"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(palindromify("race", False))

def  palindromify(word: str, isEven: bool) -> str:
"""This function 'palindromifies' a word"""
    newEnding: str = ""
    isEven: bool
    i: int = len(word)-1
    if isEven: 
        while i >= 0:
            temp: chr = word[i]
            newEnding += temp
            i -= 1
    else:
        while i >= 1:
            temp: chr = word[i-1]
            newEnding += temp
            i -= 1
    return word + newEnding

if __name__ == "__main__":
    main()