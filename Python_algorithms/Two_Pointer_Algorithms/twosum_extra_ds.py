from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    """
    Read inputs from stdin and return them as a tuple.
    """
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_num = int(input())
    return arr, target_num


def twosum_extra_ds(numbers, X):
    """
    Find two elements in the given list of numbers that add up to the target value using an extra data structure.

    :param numbers: The list of numbers to search in.
    :param X: The target value to find a pair of numbers that add up to it.
    :return: The pair of numbers that add up to the target value, or None if not found.
    """
    # Create a set to store previous numbers and use it for faster lookup.
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # If no pair of numbers is found, return None.
    return None


arr, target_num = read_input()
result = twosum_extra_ds(arr, target_num)
if result is None:
    print(None)
else:
    print(*result)
