def reverse_string(s: str) -> str:
    """
    Reverse the given string.

    Args:
        s: The input string.

    Returns:
        The reversed string.

    Raises:
        TypeError: If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]


if __name__ == "__main__":
    examples = ["hello", "", "a", "Madam, I'm Adam", "12345", "  spaced  "]
    for text in examples:
        print(f"{text!r} -> {reverse_string(text)!r}")