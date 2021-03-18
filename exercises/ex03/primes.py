"""EX03 - prime functions."""

__author__: str = "730387741"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(1))
    print(list_primes(1, 100))


def is_prime(x: int) -> bool:
    """This function determines if a number is prime."""
    i: int = 2
    while i < 9:
        if x == 1:
            return False
        if x == 0:
            return False
        if x % i == 0:
            if i != x:
                return False
            else:
                i += 1
        else:
            i += 1
    return True


def list_primes(x: int, y: int) -> list[int]:
    """This function lists all prime number between two given integers."""
    primes: list[int] = []
    cur: int = x
    while cur < y:
        if is_prime(cur):
            primes.append(cur)
            cur += 1
        else:
            
            cur += 1
    return primes


if __name__ == "__main__":
    main()