def reverse_string(s: str) -> str:
    """
    Reverses the given string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

if __name__ == "__main__":
    # Example usage
    original_text = "Hello, World!"
    reversed_text = reverse_string(original_text)
    
    print(f"Original: '{original_text}'")
    print(f"Reversed: '{reversed_text}'")
    
    # Edge cases
    print(f"Empty string: '{reverse_string('')}'")
    print(f"Single character: '{reverse_string('A')}'")