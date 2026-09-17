def binary_search(arr, target):
    """
    Perform binary search on a sorted list.

    Args:
        arr: A list of comparable elements sorted in ascending order.
        target: The value to search for.

    Returns:
        The index of target in arr if found, otherwise -1.

    Raises:
        TypeError: If arr is not a list/sequence.
    """
    if not hasattr(arr, "__len__") or not hasattr(arr, "__getitem__"):
        raise TypeError("arr must be a sequence (e.g., list or tuple)")

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print(binary_search(numbers, 7))   # Output: 3
    print(binary_search(numbers, 1))   # Output: 0
    print(binary_search(numbers, 19))  # Output: 9
    print(binary_search(numbers, 4))   # Output: -1
    print(binary_search([], 5))        # Output: -1