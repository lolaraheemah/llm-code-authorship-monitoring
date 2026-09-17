def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    return text == text[::-1]


# Example
word = "madam"
print(is_palindrome(word))  # True