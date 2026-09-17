def word_frequency(text):
    """Return a dictionary containing the frequency of each word."""
    words = text.lower().split()
    frequency = {}

    for word in words:
        # Remove common punctuation around words
        word = word.strip(".,!?;:'\"()[]{}")
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


# Example
text = "Hello world! Hello Python. Python is great."
print(word_frequency(text))
# Output: {'hello': 2, 'world': 1, 'python': 2, 'is': 1, 'great': 1}