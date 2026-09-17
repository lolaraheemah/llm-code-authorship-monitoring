def second_largest(numbers):
    """
    Return the second largest unique value in a list of numbers.

    Raises:
        ValueError: if the list has fewer than 2 unique values.
    """
    if not numbers:
        raise ValueError("List must contain at least two unique numbers.")

    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two unique numbers.")

    largest = second = float('-inf')
    for num in unique_numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second


if __name__ == "__main__":
    data = [4, 1, 7, 7, 3, 9, 9, 2]
    print("Second largest:", second_largest(data))  # Expected: 7

    try:
        second_largest([5])
    except ValueError as e:
        print("Error:", e)