"""EX03 - prime functions."""

__author__: str = "730387741"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(1))
    print(list_primes(10, 20))

def is_prime(x: int) -> bool:
    """This function determines if a number is prime."""
    i: int = 2
    x: int
    while i < 9:
        if x == 1:
            return True
        if x % i == 0:
            if i != x:
                return True
            else:
                i+=1
        else:
            i+=1
    return False

def list_primes(x: int, y: int) -> list:
    """This function lists all prime number between two given integers."""
    primes: list = []
    cur: int = x
    while cur < y:
        if is_prime(cur):
            cur += 1
        else:

            primes.append(cur)
            cur+=1
    return primes

if __name__ == "__main__":
    main()