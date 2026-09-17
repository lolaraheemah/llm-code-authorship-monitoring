def remove_duplicates(items):
    """
    Remove duplicate elements from an iterable while preserving order.

    Args:
        items: An iterable of hashable elements.

    Returns:
        A list with duplicates removed, preserving first occurrence order.
    """
    if items is None:
        return []

    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    example = [1, 2, 2, 3, 1, 4, 5, 4, "a", "a", None, None]
    print(remove_duplicates(example))
    # Output: [1, 2, 3, 4, 5, 'a', None]

    print(remove_duplicates([]))
    # Output: []

    print(remove_duplicates(None))
    # Output: []