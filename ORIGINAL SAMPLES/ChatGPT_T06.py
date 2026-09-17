def second_largest(numbers):
    """
    Return the second largest distinct number in a list.

    Raises:
        ValueError: If there are fewer than two distinct values.
    """
    unique = set(numbers)

    if len(unique) < 2:
        raise ValueError("At least two distinct numbers are required.")

    largest = max(unique)
    unique.remove(largest)

    return max(unique)


# Example
numbers = [10, 5, 8, 10, 3, 8]
print(second_largest(numbers))  # 8