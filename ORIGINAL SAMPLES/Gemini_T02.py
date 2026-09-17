def is_palindrome(s) -> bool:
    """
    Checks if the given input is a palindrome.
    Ignores non-alphanumeric characters and case.
    """
    if not isinstance(s, str):
        s = str(s)
        
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "",
        "12321",
        12321,
        "No 'x' in Nixon"
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f"{repr(test):<35} -> {result}")