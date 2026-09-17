def binary_search(arr, target):
    """Return the index of target in a sorted array, or -1 if not found."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(numbers, target)
print(result)  # Output: 3