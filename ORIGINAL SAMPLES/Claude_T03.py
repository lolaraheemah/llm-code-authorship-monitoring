import re
from collections import Counter


def word_frequency(text):
    """
    Count the frequency of each word in the given text.

    - Case-insensitive
    - Ignores punctuation
    - Returns a dictionary sorted by descending frequency, then alphabetically
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    words = re.findall(r"[a-zA-Z']+", text.lower())
    words = [w.strip("'") for w in words if w.strip("'")]

    counts = Counter(words)

    sorted_counts = dict(
        sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    )
    return sorted_counts


if __name__ == "__main__":
    sample_text = "The quick brown fox jumps over the lazy dog. The dog barks!"
    result = word_frequency(sample_text)
    for word, freq in result.items():
        print(f"{word}: {freq}")

    print(word_frequency(""))