"""EX03 - palindromify function."""

__author__: str = "730387741"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("han", True))


def  palindromify(word: str, isEven: bool) -> str:
    """This function 'palindromifies' a word."""
    newEnding: str = ""
    i: int = len(word) - 1
    temp: str
    if isEven: 
        while i >= 0:
            temp = word[i]
            newEnding += temp
            i -= 1
    else:
        while i >= 1:
            temp = word[i - 1]
            newEnding += temp
            i -= 1
    return word + newEnding


if __name__ == "__main__":
    main()