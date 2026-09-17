def remove_duplicates(items):
    """Return a list with duplicates removed while preserving order."""
    result = []
    seen = set()

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Example
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
print(remove_duplicates(numbers))
# Output: [1, 2, 3, 4, 5]