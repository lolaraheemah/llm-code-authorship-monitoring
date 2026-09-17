def binary_search(arr: list, target: int | float) -> int:
    """
    Searches for a target value within a sorted list using the binary search algorithm.
    
    Args:
        arr: A list of sorted elements (numbers, strings, etc. that support comparison).
        target: The element to search for.
        
    Returns:
        The index of the target if found, otherwise -1.
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
if __name__ == "__main__":
    # A sorted list of numbers
    sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # Test case 1: Target exists in the list
    target_1 = 23
    result_1 = binary_search(sorted_data, target_1)
    print(f"Searching for {target_1}: Found at index {result_1}")
    
    # Test case 2: Target does not exist in the list
    target_2 = 10
    result_2 = binary_search(sorted_data, target_2)
    print(f"Searching for {target_2}: Found at index {result_2}")
    
    # Test case 3: Edge case - Empty list
    empty_list = []
    target_3 = 5
    result_3 = binary_search(empty_list, target_3)
    print(f"Searching in an empty list: Found at index {result_3}")