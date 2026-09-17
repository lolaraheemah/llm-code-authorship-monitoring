def remove_duplicates(iterable):
    """
    Removes duplicates from an iterable while preserving the original order.
    Robustly handles both hashable (e.g., int, str) and unhashable (e.g., list, dict) elements.
    """
    if not iterable:
        return []
        
    seen_hashable = set()
    seen_unhashable = []
    result = []
    
    for item in iterable:
        try:
            # Attempt to handle as a hashable item
            if item not in seen_hashable:
                seen_hashable.add(item)
                result.append(item)
        except TypeError:
            # Fallback for unhashable items (like lists or dicts)
            if item not in seen_unhashable:
                seen_unhashable.append(item)
                result.append(item)
                
    return result


if __name__ == "__main__":
    # Example 1: Standard hashable items (integers and strings)
    numbers = [1, 2, 3, 2, 4, 1, 5, "apple", "apple"]
    print("Original:", numbers)
    print("Deduplicated:", remove_duplicates(numbers))
    print("-" * 40)
    
    # Example 2: Unhashable items (nested lists and dicts)
    complex_data = [[1, 2], {"a": 1}, [1, 2], [3, 4], {"a": 1}]
    print("Original:", complex_data)
    print("Deduplicated:", remove_duplicates(complex_data))
    print("-" * 40)
    
    # Example 3: Edge cases (empty list and string)
    print("Empty list:", remove_duplicates([]))
    print("String deduplication:", remove_duplicates("abracadabra"))
    print("None input:", remove_duplicates(None))