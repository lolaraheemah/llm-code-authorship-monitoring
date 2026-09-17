def second_largest(numbers):
    """
    Finds the second largest number in a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        int or float: The second largest number in the list.
        None: If the list has fewer than two distinct elements.
    """
    if not numbers or len(numbers) < 2:
        return None

    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    return second_largest

# Example usage:
if __name__ == '__main__':
    numbers_list = [10, 5, 8, 20, 15, 20]
    result = second_largest(numbers_list)
    print(f"The second largest number in {numbers_list} is: {result}")

    # Edge cases
    empty_list = []
    print(f"Second largest in {empty_list}: {second_largest(empty_list)}")

    single_element_list = [5]
    print(f"Second largest in {single_element_list}: {second_largest(single_element_list)}")
    
    all_same_list = [7, 7, 7, 7]
    print(f"Second largest in {all_same_list}: {second_largest(all_same_list)}")