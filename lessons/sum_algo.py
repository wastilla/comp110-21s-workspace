"""Examples of list and loop algorithm."""

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned."""
    # 1. Initialize total and index i to 0
    total: int = 0
    i: int = 0
    # 2. While index i is valid, meaning i < len(xs)
    while i < len(xs):
        # 2. True) take xs[i] and add to total
        total += xs[i]
        # 2. True) increase i by 1, moving it to next index variable
        i += 1
    #   2. False) Result is stored in total varible
    return total

odds: list[int] = []
odds_sum: int = sum_algo(odds)
print(odds_sum)