from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    """
    Reads input from the user.

    Returns:
        A tuple containing a list of integers and a target integer.
    """
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_num = int(input())
    return arr, target_num


def twosum_with_sort(numbers, X):
    """
    Finds a pair of integers in the given list of integers that add up to the given target number.

    This function uses a two-pointer approach where the array is first sorted in non-descending order. Two pointers
    are then initialized at the beginning and end of the array, respectively. The two pointers move towards each
    other until they meet, checking if the sum of the two pointers is equal to the target number.

    Args:
        numbers: A list of integers to search for a pair.
        X: The target integer to find a pair that adds up to.

    Returns:
        A tuple containing a pair of integers that add up to the target number, or None if no such pair exists.
    """
    # Sort the given array in non-descending order
    numbers.sort()

    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(numbers) - 1

    # Move the pointers towards each other until they meet
    while left < right:
        current_sum = numbers[left] + numbers[right]

        # If the sum of the two pointers is equal to the target number, return the pair of integers
        if current_sum == X:
            return numbers[left], numbers[right]

        # If the sum is less than the target number, move the left pointer to the right
        if current_sum < X:
            left += 1

        # If the sum is greater than the target number, move the right pointer to the left
        else:
            right -= 1

    # If no pair of integers that add up to the target number is found, return None
    return None


# Read input from the user
arr, target_num = read_input()

# Call the twosum_with_sort function and store the result
result = twosum_with_sort(arr, target_num)

# Print the result
if result is None:
    print(None)
else:
    print(*result)
