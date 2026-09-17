def is_palindrome(s: str) -> bool:
    """
    Check whether a given string is a palindrome, ignoring
    case, spaces, and punctuation.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    examples = [
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "Hello, World!",
        "",
        "12321",
        "No lemon, no melon"
    ]

    for text in examples:
        print(f"{text!r} -> {is_palindrome(text)}")